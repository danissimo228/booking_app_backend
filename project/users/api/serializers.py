from rest_framework import serializers
from utils.choices import GenderChoices
from config.settings import TOKEN_RECOVER_LENGTH


class RequestCreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField(required=False, allow_null=True)
    password = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, min_length=9)
    gender = serializers.ChoiceField(choices=GenderChoices.choices)
    geolocation = serializers.CharField()
    date_of_birthday = serializers.DateField()


class UserProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField(required=False, allow_null=True)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, min_length=9)
    gender = serializers.ChoiceField(choices=GenderChoices.choices)
    geolocation = serializers.CharField()
    date_of_birthday = serializers.DateField()
    photo_url = serializers.CharField(required=False, allow_null=True)
    rating = serializers.IntegerField(default=0)
    last_login = serializers.DateTimeField(required=False, allow_null=True)


class RecoverUsersPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecoverTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(min_length=TOKEN_RECOVER_LENGTH, max_length=40)
    new_password = serializers.CharField(min_length=5)
    is_active = serializers.BooleanField(default=True)
