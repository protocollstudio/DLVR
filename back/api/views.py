from django.shortcuts import render
from rest_framework import generics
from tracks.models import Track
from .serializers import TrackSerializer


class TrackAPIView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

