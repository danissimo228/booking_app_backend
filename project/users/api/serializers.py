from rest_framework import serializers
from utils.choices import GenderChoices
from config.settings import TOKEN_RECOVER_LENGTH


class RequestCreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    middle_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    password = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, min_length=9, required=False, allow_null=True)
    gender = serializers.ChoiceField(choices=GenderChoices.choices, required=False, allow_blank=True, allow_null=True)
    geolocation = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    date_of_birthday = serializers.DateField(required=False, allow_null=True)


class ResponseUserProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    middle_name = serializers.CharField(required=False, allow_null=True)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, min_length=9, required=False, allow_null=True)
    gender = serializers.ChoiceField(choices=GenderChoices.choices, allow_null=True)
    geolocation = serializers.CharField(required=False, allow_null=True)
    date_of_birthday = serializers.DateField(required=False, allow_null=True)
    photo_url = serializers.CharField(required=False, allow_null=True)
    rating = serializers.IntegerField(default=0)
    last_login = serializers.DateTimeField(required=False, allow_null=True)


class RequestRecoverUsersPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RequestRecoverTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(min_length=TOKEN_RECOVER_LENGTH, max_length=40)
    new_password = serializers.CharField(min_length=5)
    is_active = serializers.BooleanField(default=True)


class RequestSetAttrUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    middle_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    phone = serializers.CharField(max_length=15, min_length=9, required=False, allow_blank=True, allow_null=True)
    gender = serializers.ChoiceField(choices=GenderChoices.choices, required=False, allow_blank=True, allow_null=True)
    geolocation = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    photo_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    date_of_birthday = serializers.DateField(required=False, allow_null=True)


class RequestSubscribeToUserSerializer(serializers.Serializer):
    subscribe_user_id = serializers.IntegerField(min_value=1)
