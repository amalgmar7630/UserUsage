import django_filters
from django_filters import OrderingFilter

from usage.models import Usage


class UsageFilter(django_filters.FilterSet):
    order = OrderingFilter(
        fields=(
            ('usage_at', 'usage_at'),
        ),
    )

    class Meta:
        model = Usage
        fields = {
            'usage_at': ['lte', 'gte', 'lt', 'gt']
        }
