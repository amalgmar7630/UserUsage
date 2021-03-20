from rest_framework.serializers import ModelSerializer

from usage_types.models import UsageType


class UsageTypesSerializer(ModelSerializer):
    class Meta:
        model = UsageType
        fields = '__all__'
