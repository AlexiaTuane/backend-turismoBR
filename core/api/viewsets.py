from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoturisticoSerializer


class PontoturisticoViewSet(ModelViewSet):
    serializer_class = PontoturisticoSerializer
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    