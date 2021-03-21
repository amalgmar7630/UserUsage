from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from usage.models import Usage
from usage_types.models import UsageType
from usage_types.serializers import UsageTypesSerializer
from users.models import User


class UsagesSerializer(ModelSerializer):
    usage_type_assigned = UsageTypesSerializer(many=False, allow_null=True, source='usage_type')

    class Meta:
        model = Usage
        fields = ('id', 'usage_at', 'usage_type_assigned',)


class UsagesUserSerializer(UsagesSerializer):
    class Meta(UsagesSerializer.Meta):
        exclude = None
        fields = UsagesSerializer.Meta.fields + ('user_id',)


class CreateOrUpdateUsageSerializer(ModelSerializer):
    usage_at = serializers.DateTimeField()
    usage_type = serializers.PrimaryKeyRelatedField(queryset=UsageType.objects.all(), many=False)

    class Meta:
        model = Usage
        fields = ('usage_at', 'usage_type', )


class CreateOrUpdateUsageUserSerializer(CreateOrUpdateUsageSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta(CreateOrUpdateUsageSerializer.Meta):
        exclude = None
        fields = CreateOrUpdateUsageSerializer.Meta.fields + ('user',)
