from rest_framework import viewsets

from usage.models import Usage
from usage.serializers import UsageSerializer


class UsageViewSet(viewsets.ModelViewSet):
    serializer_class = UsageSerializer
    queryset = Usage.objects.all()
