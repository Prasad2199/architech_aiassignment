from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContentItem
from .serializers import ContentItemSerializer

@api_view(['POST'])
def create_content(request):
    serializer = ContentItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)  # Assuming user is authenticated
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_content(request, pk):
    content = ContentItem.objects.get(pk=pk)
    serializer = ContentItemSerializer(content)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_content(request, pk):
    content = ContentItem.objects.get(pk=pk)
    serializer = ContentItemSerializer(instance=content, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_content(request, pk):
    content = ContentItem.objects.get(pk=pk)
    content.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
