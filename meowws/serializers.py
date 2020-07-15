from rest_framework import serializers
from django.conf import settings
from .models import Meoww

MAX_MEOWW_LENGTH = settings.MAX_MEOWW_LENGTH


class MeowwSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meoww
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_MEOWW_LENGTH:
            raise serializers.ValidationError("Tweet too long")
        return value
