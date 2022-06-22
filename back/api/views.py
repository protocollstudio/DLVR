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
    lookup_field = "ID"


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    lookup_field = "ID"


@api_view(["GET"])
def add_like(request, uuid):
    try:
        track = Track.objects.get(uuid=uuid)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TrackSerializer(track)
        lookup_field = "ID"
        track.likes += 1
        track.save()
        return Response(serializer.data)



@api_view(["GET"])
def add_dislike(request, uuid):
    try:
        track = Track.objects.get(uuid=uuid)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TrackSerializer(track)
        lookup_field = "ID"
        track.dislikes += 1
        track.save()
        return Response(serializer.data)
