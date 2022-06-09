from django.urls import path
from .views import TrackAPIView, TrackDetail, add_like, add_dislike


urlpatterns = [
        path("", TrackAPIView.as_view()),
        path("<int:pk>/", TrackDetail.as_view()),
        path("<int:pk>/like", add_like),
        path("<int:pk>/dislike", add_dislike),
        ]
