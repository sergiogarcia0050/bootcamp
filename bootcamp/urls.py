"""
URL configuration for bootcamp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from courses import urls as courses_urls
from events import urls as events_urls
from people import urls as person
from knowledge_suppliers import urls as knowledge
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from front import urls as login
from people.views.person import CustomTokenObtainPairView


urlpatterns = [
    path('', include(login)),
    path('admin/', admin.site.urls),
    path('courses/', include(courses_urls)),
    path('events/', include(events_urls)),
    path('people/', include(person)),
    path('knowledge_suppliers/', include(knowledge)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
