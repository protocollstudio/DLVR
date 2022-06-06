from django.urls import path
from .views import TrackAPIView


urlpatterns = [
        path("", TrackAPIView.as_view()),
        ]
