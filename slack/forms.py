from django import forms
from .models import UserCreate

class ChatTextModel(forms.ModelForm):
    class Meta:
        model = UserCreate
        fields = "__all__"

     