from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from usage.filtersets import UsageFilter
from usage.models import Usage
from usage.serializers import CreateOrUpdateUsageSerializer
from users.models import User
from users.serializers import UsersSerializer, UsagesSerializer


class UsersViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class CurrentUserUsagesViewSet(viewsets.ModelViewSet):
    serializer_class = CreateOrUpdateUsageSerializer
    filterset_class = UsageFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UsagesSerializer
        return self.serializer_class

    def get_queryset(self):
        return Usage.objects.select_related('usage_type').filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        super(CurrentUserUsagesViewSet, self).perform_create(serializer)
        serializer.save(user=self.request.user)
