from rest_framework.viewsets import ModelViewSet
from endereco.models import enderecos
from .serializers import EnderecoSerializer


class EnderecosViewSet(ModelViewSet):
    queryset = enderecos.objects.all()
    serializer_class = EnderecoSerializer

    