from rest_framework import viewsets

from usage.filtersets import UsageFilter
from usage.models import Usage
from usage.serializers import CreateOrUpdateUsageSerializer
from users.models import User
from users.serializers import UsersSerializer, UsagesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    http_method_names = ['get']


class CurrentUserUsagesViewSet(viewsets.ModelViewSet):
    serializer_class = CreateOrUpdateUsageSerializer
    queryset = Usage.objects.all()
    filterset_class = UsageFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UsagesSerializer
        return self.serializer_class

    def get_queryset(self):
        return Usage.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer, commit=True):
        super(CurrentUserUsagesViewSet, self).perform_create(serializer)
        serializer.save(user=self.request.user)
