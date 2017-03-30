from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from keystoneauth1 import loading
from keystoneauth1 import session

from serializers import UserSerializer

# Create your views here.

# ViewSets define the view behavior.
from rest_framework import viewsets
from heatclient import client


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

tenant_id = 'b363706f891f48019483f8bd6503c54b'
heat_url = 'http://heat.example.org:8004/v1/%s' % tenant_id
auth_token = '3bcc3d3a03f44e3d8377f9247b0ad155'



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def app(request):
    lista = [
        "ALIMENTACAO",
        "ANIMAIS",
        "AULAS",
        "AUTOMOTIVO",
        "BELEZA_E_BEM_ESTAR",
        "CASA_E_CONSTRUCAO",
        "COMUNICACAO_E_ARTES",
        "CONSULTORIA",
        "DELIVERY",
        "EVENTOS_E_MUSICA",
        "SAUDE",
        "TECNOLOGIA",
        "TRANSPORTE",
        "SEGURANCA",
        "OUTROS"]
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(auth_url='http://180.10.10.51:35357/v3',
    username='admin',
    password='ADMIN_PASS',
    user_domain_name='default',
    project_id='04a4ea69b5054d0b855f09c6ba275b06')
    sess = session.Session(auth=auth)
    heat = client.Client('1', session=sess)
    stacks = heat.stacks
    stacks.create()
    #print(next(heat.stacks.list()))
    return Response({"ok"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def post_app(request):
    """
    Iniciar aplicacao do openstack
    """
    return Response({"Post executado"}, status=status.HTTP_200_OK)
