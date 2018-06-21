from django import forms
from markdownx.fields import MarkdownxFormField


class MarkdownEditor(forms.Form):
    text = MarkdownxFormField()
