from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from usage.viewsets import UsageViewSet

router = routers.DefaultRouter()
router.register(r'', UsageViewSet)

app_name = "usages"

urlpatterns = [
    url(r'^', include(router.urls)),
]