from django.shortcuts import render
from .models import Track
from django.views.generic import ListView


class TrackListView(ListView):
    model = Track
    template_name = "track_list.html"
