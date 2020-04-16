from rest_framework import serializers

from . import models

class HumanSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=False)
    class Meta():
        model = models.Human
        fields = '__all__'