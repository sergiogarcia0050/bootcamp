from django.urls import path, include
from rest_framework.routers import DefaultRouter
from front.views.login.login import loginview


urlpatterns = [
    path('login/', loginview)
]



