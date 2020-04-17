from django import forms
from .models import ModelClass


class ModelForm(forms.ModelForm):
    class Meta:
        model = ModelClass
        fields = '__all__'
