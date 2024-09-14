from django.urls import path
from .views import RegisterViewSet, GetMeViewSet, ChangePasswordViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r"register", RegisterViewSet, basename="register")
router.register(r"me", GetMeViewSet, basename="me")
router.register(r"change-password", ChangePasswordViewSet, basename="change-password")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
