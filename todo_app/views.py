from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Create':'/task-create/',
    }

    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)
    