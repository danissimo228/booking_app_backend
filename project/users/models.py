from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.choices import GenderChoices
from utils.mixins.model_mixin import CreatedUpdatedModelMixin
from project.users.managers import UserManager
from django.core.validators import MinValueValidator, MaxValueValidator


class Users(AbstractUser):
    """Custom user model"""
    objects = UserManager()

    middle_name = models.CharField(null=True, max_length=150, blank=True)
    username = models.CharField(max_length=15, unique=True, null=False)
    email = models.EmailField("email address", null=True, unique=True, db_index=True)
    phone = models.CharField(max_length=15, null=False, db_index=True)
    gender = models.CharField(max_length=100, choices=GenderChoices.choices, null=False)
    geolocation = models.CharField(max_length=255, null=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0, null=False)
    photo_url = models.CharField(null=True, default=None, blank=True)
    date_of_birthday = models.DateField(null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_permissions_related'
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='user_groups'
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} {self.username}"


class Subs(CreatedUpdatedModelMixin):
    sub = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="sub_id")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="user_id")

    def __str__(self):
        return f"sub: {self.sub}; user: {self.user}"


class RecoverPasswordData(CreatedUpdatedModelMixin):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="user")
    token = models.TextField(null=False, unique=True)
    expiration_time = models.DateTimeField()



