
from rest_framework import serializers
from knowledge_suppliers.models import knowledgeSupplier
from rest_framework import viewsets

class kowledSupplierSerializer(serializers.ModelSerializer):

	class Meta:
			model = knowledgeSupplier
			fields = "__all__"


class KnowledgeSpplierViewSet(viewsets.ModelViewSet):
    queryset = knowledgeSupplier.objects.all()
    serializer_class = kowledSupplierSerializer



