from rest_framework import serializers
from django.conf import settings
from .models import Meoww

MAX_MEOWW_LENGTH = settings.MAX_MEOWW_LENGTH
MEOWW_ACTION_OPTION = settings.MEOWW_ACTION_OPTION


class MeowwActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in MEOWW_ACTION_OPTION:
            raise serializers.ValidationError("Invalid Action for Meoww!")
        return value


class MeowwSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Meoww
        fields = ['id', 'content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_MEOWW_LENGTH:
            raise serializers.ValidationError("Tweet too long")
        return value
