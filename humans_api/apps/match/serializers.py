from rest_framework import serializers

from . import models
from human.models import Human
from human.serializers import HumanSerializer


class MatchSeializer(serializers.ModelSerializer):
    class Meta():
        model = models.Match
        exclude = ['human']

class MatchWithNestedHumanSeializer(serializers.ModelSerializer):
    human = HumanSerializer()
    
    class Meta():
        model = models.Match
        fields = "__all__"

class HumanMatchSerializer(serializers.ModelSerializer):
    match = MatchSeializer()

    class Meta():
        model = Human
        fields = "__all__"