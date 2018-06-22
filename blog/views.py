from django.shortcuts import render, redirect
from django.conf import settings

from .models import Post
from .forms import NewPostForm

import os
import glob


def index(request):
    latest_post_list = Post.objects.order_by('-travel_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)


def gallery(request):
    images = _get_images_ending_with(".jpg") + _get_images_ending_with(".png")
    images = [i.replace(settings.MEDIA_ROOT, settings.MEDIA_URL, 1)
              for i in images]
    context = {
            "images": images,
            }
    return render(request, 'blog/gallery.html', context)


def _get_images_ending_with(extension):
    return glob.glob(os.path.join(
        settings.MEDIA_ROOT, "markdownx", "*", "*", "*", "*" + extension))


def new(request):
    if request.method == 'POST':
        post_author = request.user
        post = Post(author=post_author)
        form_data = NewPostForm(request.POST, instance=post)
        if form_data.is_valid():
            form_data.clean()
            form_data.save()
            return redirect('blog:index')
    else:
        post_form = NewPostForm()
        context = {'post_form': post_form}
        template = 'blog/new.html'
        return render(request, template, context)
