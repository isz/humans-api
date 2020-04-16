from django.core.exceptions import ValidationError
from django.db import models

MIN_VALID_AGE = 0   #
MAX_VALID_AGE = 140 # Current record 122 years

class Gender(models.TextChoices):
    MALE = "male"
    FEMALE = "female"

def validate_age(age):
    if age < MIN_VALID_AGE:
        raise ValidationError('Too yang')
    if age > MAX_VALID_AGE:
        raise ValidationError('Too old')


class Human(models.Model):
    avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars")
    first_name = models.CharField(verbose_name="First Name", max_length=32)
    second_name = models.CharField(verbose_name="Second Name", max_length=32)
    age = models.PositiveIntegerField(verbose_name="Age", validators=[validate_age])
    gender = models.CharField(
        verbose_name="Gender",
        max_length=len(max(Gender.values, key=lambda i: len(i))),
        choices=Gender.choices,
    )
