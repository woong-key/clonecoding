# 2021.04.29 김인웅
from .models import Scene
from django import forms

class SceneForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = ['scene_content', 'scene_password']