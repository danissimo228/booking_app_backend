from utils.mixins.response_mixins import ResponseModelViewSetMixin
from rest_framework.permissions import AllowAny
from project.users.api import serializers
from django.forms.models import model_to_dict
from ..models import Users, RecoverPasswordData
from utils.decorator import log_viewset_action
from drf_spectacular.utils import extend_schema
import utils.serializers as util_serializer
import logging
import secrets
from django.utils import timezone
from utils.email import send_email
from config.settings import TOKEN_RECOVER_LENGTH, ACCESS_TOKEN_LIFETIME, DAY_LIMIT_TO_CHANGE_PASSWORD

logger = logging.getLogger(__name__)


class UsersModelViewSet(ResponseModelViewSetMixin):
    permission_classes = [AllowAny]

    @extend_schema(
        request=serializers.RequestCreateUserSerializer,
        responses={
            200: serializers.UserProfileSerializer,
            400: util_serializer.NormalAnswerSerializer,
            401: util_serializer.TokenErrorSerializer,
            404: util_serializer.NormalAnswerSerializer,
        },
    )
    @log_viewset_action(logger)
    def create_user(self, request, *args, **kwargs):
        data = self.serialize_request(serializers.RequestCreateUserSerializer, request.data)

        if Users.objects.filter(email=data["email"]).exists() or Users.objects.filter(email=data["username"]).exists():
            return self.error_response(400, "User already exists")

        created_user = Users.objects.create_user(**data)

        return self.success_response(
            self.serialize_request(serializers.UserProfileSerializer, model_to_dict(created_user))
        )

    @extend_schema(
        request=serializers.RecoverUsersPasswordSerializer,
        responses={
            200: util_serializer.NormalAnswerSerializer,
            400: util_serializer.NormalAnswerSerializer,
            401: util_serializer.TokenErrorSerializer,
            404: util_serializer.NormalAnswerSerializer,
        },
    )
    @log_viewset_action(logger)
    def recover(self, request, *args, **kwargs):
        data = self.serialize_request(serializers.RecoverUsersPasswordSerializer, request.data)
        email = data["email"]
        today = str(timezone.now()).split(" ")[0]
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist as ex:
            return self.error_response(400, ex)

        users_recover = RecoverPasswordData.objects.filter(user=user)
        if len(users_recover) >= DAY_LIMIT_TO_CHANGE_PASSWORD:
            recover_times = [
                str(recover.created_at) for recover in users_recover if str(recover.created_at).split(" ")[0] == today
            ]
            if len(recover_times) >= DAY_LIMIT_TO_CHANGE_PASSWORD:
                return self.error_response(
                    400, "You have changed your password too many times today, try again tomorrow"
                )

        token = secrets.token_hex(TOKEN_RECOVER_LENGTH)
        RecoverPasswordData.objects.create(
            user=user, token=token, expiration_time=ACCESS_TOKEN_LIFETIME + timezone.now()
        )
        send_email(token=token, email_to=email)
        return self.success_response()

    @extend_schema(
        request=serializers.RecoverTokenSerializer,
        responses={
            200: util_serializer.NormalAnswerSerializer,
            400: util_serializer.NormalAnswerSerializer,
            401: util_serializer.TokenErrorSerializer,
            404: util_serializer.NormalAnswerSerializer,
        },
    )
    @log_viewset_action(logger)
    def change_password(self, request, *args, **kwargs):
        data = self.serialize_request(serializers.RecoverTokenSerializer, request.data)
        recover_data = RecoverPasswordData.objects.filter(token=data["token"]).first()

        if not recover_data:
            return self.error_response(400, "Not a valid token")

        if recover_data.expiration_time < timezone.now():
            return self.error_response(400, "Not a valid token")

        user = recover_data.user
        if data["email"] != user.email:
            self.error_response(400, "Not a valid email")

        recover_data.is_active = False
        recover_data.save()
        user.set_password(data["new_password"])
        user.save()

        return self.success_response()

    @extend_schema(
        responses={
            200: serializers.UserProfileSerializer,
            400: util_serializer.NormalAnswerSerializer,
            401: util_serializer.TokenErrorSerializer,
            404: util_serializer.NormalAnswerSerializer,
        },
    )
    @log_viewset_action(logger)
    def get_user_profile(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.error_response(401, "No access")
        return self.success_response(self.serialize_request(serializers.UserProfileSerializer, model_to_dict(user)))
