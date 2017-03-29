from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from serializers import UserSerializer

# Create your views here.

# ViewSets define the view behavior.
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

    return Response({"Requisicao revebida"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def post_app(request):
    """
    Iniciar aplicacao do openstack
    """
    return Response({"Post executado"}, status=status.HTTP_200_OK)
