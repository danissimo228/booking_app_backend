from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MALE = "male"
    FEMALE = "female"
    TRANS = "trans"

