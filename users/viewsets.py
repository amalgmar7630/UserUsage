from rest_framework import viewsets
from users.models import User
from users.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    http_method_names = ['get']
