from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views.course import CourseViewSet


router = DefaultRouter()

router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
