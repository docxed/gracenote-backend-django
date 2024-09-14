from django.urls import path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")


urlpatterns = [
    path("", include(router.urls)),
]
