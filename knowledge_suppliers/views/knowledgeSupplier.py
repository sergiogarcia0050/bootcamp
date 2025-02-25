
from rest_framework import serializers
from knowledge_suppliers.models import knowledge_supplier
from rest_framework import viewsets

class kowledSupplierSerializer(serializers.ModelSerializer):

	class Meta:
			model = knowledge_supplier.KnowledgeSupplier
			fields = "__all__"


class KnowledgeSpplierViewSet(viewsets.ModelViewSet):
    queryset = knowledge_supplier.KnowledgeSupplier.objects.all()
    serializer_class = kowledSupplierSerializer



