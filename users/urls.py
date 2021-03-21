from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from users.viewsets import UsersViewSet, CurrentUserUsagesViewSet

router = routers.DefaultRouter()
router.register(r'currentUserUsages', CurrentUserUsagesViewSet, basename='current_user_usage')
router.register(r'', UsersViewSet, basename='users')

app_name = "users"

urlpatterns = [
    url(r'^', include(router.urls)),
]