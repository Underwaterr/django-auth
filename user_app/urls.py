from django.urls import path, include

from rest_framework import routers
from .views import UserViewSet, login_view, get_csrf_token, CheckAuth

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view),
    path('get-csrf-token/', get_csrf_token)
]

