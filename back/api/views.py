from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tracks.models import Track
from .serializers import TrackSerializer
from django.http import HttpResponse


class TrackAPIView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


@api_view(["GET"])
def add_like(request, pk):
    try:
        track = Track.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TrackSerializer(track)
        track.likes += 1
        track.save()
        return Response(serializer.data)



@api_view(["GET"])
def add_dislike(request, pk):
    try:
        track = Track.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TrackSerializer(track)
        track.dislikes += 1
        track.save()
        return Response(serializer.data)
