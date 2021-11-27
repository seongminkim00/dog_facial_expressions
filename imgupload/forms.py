from django import forms
from .models import *

class ImgForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'dog_image']
