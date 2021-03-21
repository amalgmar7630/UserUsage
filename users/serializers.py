from rest_framework.serializers import ModelSerializer
from usage.serializers import UsagesSerializer
from users.models import User


class UsersSerializer(ModelSerializer):
    user_usages = UsagesSerializer(many=True, allow_null=True, source='usages')

    class Meta:
        model = User
        fields = ('id', 'name', 'user_usages',)
