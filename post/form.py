from django import forms
from .models import Entry


class Entryform(forms.ModelForm):
    class Meta:
        model=Entry
        fields="__all__"
        