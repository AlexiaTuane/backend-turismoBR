from rest_framework.serializers import ModelSerializer
from endereco.models import enderecos


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = enderecos
        fields = ('id','linha1','linha2','cidade','estado','pais','latitude','longitude')