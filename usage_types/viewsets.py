from rest_framework import viewsets

from usage_types.models import UsageType
from usage_types.serializers import UsageTypesSerializer


class UsageTypesViewSet(viewsets.ModelViewSet):
    serializer_class = UsageTypesSerializer
    queryset = UsageType.objects.all()
