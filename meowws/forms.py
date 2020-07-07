from django import forms

from .models import Meoww

MAX_LENGTH = 240


class MeowwForm(forms.ModelForm):
    class Meta:
        model = Meoww
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError("Tweet too long")
        return content
