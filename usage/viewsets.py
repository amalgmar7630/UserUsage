from rest_framework import viewsets

from usage.filtersets import UsageFilter
from usage.models import Usage
from usage.serializers import UsagesUserSerializer, CreateOrUpdateUsageUserSerializer


class UsageViewSet(viewsets.ModelViewSet):
    serializer_class = CreateOrUpdateUsageUserSerializer
    queryset = Usage.objects.all()
    filterset_class = UsageFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UsagesUserSerializer
        return self.serializer_class
