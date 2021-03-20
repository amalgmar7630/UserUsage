from rest_framework.serializers import ModelSerializer
from users.models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
