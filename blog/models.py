from django.db import models
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User
from django.utils import timezone
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_content = MarkdownxField()
    pub_date = models.DateTimeField('Post published', default=timezone.now)
    travel_date = models.DateField('Post travel date', default=timezone.now)
    last_edited = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    @property
    def formatted_markdown(self):
        return markdownify(self.post_content)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # One-to-many
    # relationship
    sender_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Comment published', default=timezone.now)
