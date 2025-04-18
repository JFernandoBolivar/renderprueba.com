from .models import Project
from rest_framework import viewsets, permissions, response
from .serializers import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.AllowAny]