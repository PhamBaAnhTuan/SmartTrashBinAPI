from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrashViewSet, TrashTypeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'trash', TrashViewSet)
router.register(r'trashtype', TrashTypeViewSet)

urlpatterns = [
   path('', include(router.urls))
]
