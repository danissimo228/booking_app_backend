import uuid
from django.db import models


class CreatedUpdatedModelMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="UUID",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время обновления",
    )

    class Meta:
        abstract = True
