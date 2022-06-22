from django.urls import path
from .views import TrackAPIView, TrackDetail, add_like, add_dislike


urlpatterns = [
        path("tracks/", TrackAPIView.as_view()),
        path("track/<uuid:ID>/", TrackDetail.as_view()),
        path("track/<uuid:ID>/like", add_like),
        path("track/<uuid:ID>/dislike", add_dislike),
        ]
