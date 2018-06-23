from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'travel_date', 'post_content']
        labels = {
            'title': 'Titel', 'travel_date': 'Resedatum', 'post_content': ''}
        widgets = {
            'post_content': MarkdownxFormField(),
            'travel_date': forms.SelectDateWidget(),
        }


class DeletePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class ImageUploadForm(forms.Form):
    file = forms.FileField()
