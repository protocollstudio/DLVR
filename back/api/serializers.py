from rest_framework import serializers
from tracks.models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ("ID", "title", "url", "path", "artwork", "audio_file", "likes", "dislikes")
