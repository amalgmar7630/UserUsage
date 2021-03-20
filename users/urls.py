from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from users.viewsets import UsersViewSet

router = routers.DefaultRouter()
router.register(r'', UsersViewSet)

app_name = "users"

urlpatterns = [
    url(r'^', include(router.urls)),
]