from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import SongsSerializer
from.models import Songs
@api_view(['GET','Post'])
def songs_list(request):
    if request.method == 'GET':
        supers = Songs.objects.all()
        serializer = SongsSerializer(product)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    return Response('ok')
# @api_view(['GET', 'PUT', 'DELETE'])
# def song_detail(request, pk):
#     song = get_object_or_404(Songs, pk=pk)
#     if request.method == 'GET':
#         serializer = SongsSerializer(song)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = SongsSerializer(song, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         song.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
