from django import forms
from .models import Image, Topic


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title', 'image']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
