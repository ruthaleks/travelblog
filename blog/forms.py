from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_content', 'travel_date']
        labels = {
            'title': '', 'travel_date': '', 'post_content': ''}
        widgets = {
            'post_content': MarkdownxFormField(),
            'travel_date': forms.SelectDateWidget(),
        }


class DeletePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class ImageUploadForm(forms.Form):
    file = forms.FileField(label="")
