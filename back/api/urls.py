from django.urls import path
from .views import TrackAPIView, TrackDetail, add_like, add_dislike


urlpatterns = [
        path("", TrackAPIView.as_view()),
        path("<uuid:ID>/", TrackDetail.as_view()),
        path("<uuid:ID>/like", add_like),
        path("<uuid:ID>/dislike", add_dislike),
        ]
