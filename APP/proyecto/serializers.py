from rest_framework import serializers
from .models import Project

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','description','tecnology','created_at')
        read_only_fields = ('created_at',)