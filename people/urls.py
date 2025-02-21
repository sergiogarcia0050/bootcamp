from django.urls import path, include
from rest_framework.routers import DefaultRouter
from people.views.person import PersonViewSet


router = DefaultRouter()

router.register(r'people', PersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]
