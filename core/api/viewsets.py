from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):    
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste': request.data})
    
    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['nome']})
    
    def destroy(self, request, *args, **kwargs):
        pass
