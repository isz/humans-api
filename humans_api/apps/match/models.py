from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from human.models import Human, Gender


class Match(models.Model):
    human = models.OneToOneField(
        Human, on_delete=models.CASCADE, related_name="match"
    )
    first_name = models.CharField(verbose_name="First Name", max_length=32)
    second_name = models.CharField(verbose_name="Second Name", max_length=32)
    age = models.PositiveIntegerField(verbose_name="Age")
    gender = models.CharField(
        verbose_name="Gender",
        max_length=len(max(Gender.values, key=lambda i: len(i))),
        choices=Gender.choices,
    )


@receiver(post_save, sender=Human)
def human_save_handler(sender, instance, created, **kwarg):
    if created:
        Match.objects.create(
            human=instance,
            first_name=instance.first_name,
            second_name=instance.second_name,
            age=instance.age,
            gender=instance.gender,
        )
    else:
        instance.match.first_name = instance.first_name
        instance.match.second_name = instance.second_name
        instance.match.age = instance.age
        instance.match.gender = instance.gender
    instance.match.save()
