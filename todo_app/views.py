from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TodoSerializer
from rest_framework.response import Response
from .models import TodoItem
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/task-list/',
#         'Create':'/task-create/',
#     }
#     return Response(api_urls)

class TodoList(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    