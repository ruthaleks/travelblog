from django.db import models
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    post_content = MarkdownxField()
    pub_date = models.DateTimeField('Post published', default=timezone.now)
    travel_date = models.DateTimeField('Post travel date')
    last_edited = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)


class Photo(models.Model):
    """ A photo can be displayed in multiple posts and a post can have multiple
    photos """
    post = models.ManyToManyField(Post)  # Many-to-many relationship
    file_name = models.CharField(max_length=100)
    photo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Photo published', default=timezone.now)
    travel_date = models.DateTimeField('Photo travel date')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # One-to-many
    # relationship
    sender_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Comment published', default=timezone.now)
