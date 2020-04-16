from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class HumanViewSet(ModelViewSet):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanSerializer
