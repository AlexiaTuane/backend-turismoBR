from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoturisticoViewSet
from endereco.api.viewsets import EnderecosViewSet
from atracoes.api.viewsets import AtracoesViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from users.api.viewsets import UserRegistrationView, UserViewSet, CustomObtainAuthToken

router = routers.DefaultRouter()

router.register(r'pontoturistico', PontoturisticoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecosViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/login/', CustomObtainAuthToken.as_view(), name='user-login'),
    # Remova a linha abaixo, pois a view já foi registrada usando o router
    # path('api/users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('admin/', admin.site.urls),
]
