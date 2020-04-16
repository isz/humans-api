from rest_framework import generics

from . import models
from . import serializers
from human.models import Human

class MatchListView(generics.ListAPIView):
    queryset = models.Match.objects.all()
    serializer_class = serializers.MatchWithNestedHumanSeializer

class MatchView(generics.RetrieveAPIView):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanMatchSerializer