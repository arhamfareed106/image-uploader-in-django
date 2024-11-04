from ast import mod
from attrs import field
from django import forms
from .models import Image
from uploder.myapp import models
from . import models

class ImageForm(forms.ModelForm):
            class Meta:
                models = Image
                field = '__all__'