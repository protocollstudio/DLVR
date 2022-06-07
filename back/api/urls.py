from django.urls import path
from .views import TrackAPIView, TrackDetail


urlpatterns = [
        path("", TrackAPIView.as_view()),
        path("<int:pk>/", TrackDetail.as_view()),
        ]
