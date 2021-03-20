from rest_framework.serializers import ModelSerializer

from usage.models import Usage


class UsageSerializer(ModelSerializer):
    class Meta:
        model = Usage
        fields = '__all__'
