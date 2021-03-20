from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from usage_types.viewsets import UsageTypesViewSet

router = routers.DefaultRouter()
router.register(r'', UsageTypesViewSet)

app_name = "usage_types"

urlpatterns = [
    url(r'^', include(router.urls)),
]