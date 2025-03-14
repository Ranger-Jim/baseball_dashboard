from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet

# Use Django REST Framework's router to generate API endpoints
router = DefaultRouter()
router.register(r'schedule', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all the routes from the router
]