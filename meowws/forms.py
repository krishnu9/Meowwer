from django import forms
from django.conf import settings
from .models import Meoww

MAX_MEOWW_LENGTH = settings.MAX_MEOWW_LENGTH


class MeowwForm(forms.ModelForm):
    class Meta:
        model = Meoww
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_MEOWW_LENGTH:
            raise forms.ValidationError("Tweet too long")
        return content
