from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knowledge_suppliers.views.knowledgeSupplier import KnowledgeSpplierViewSet


router = DefaultRouter()

router.register(r'knowledgeSuppliers', KnowledgeSpplierViewSet)

urlpatterns = [
    path('', include(router.urls))
]
