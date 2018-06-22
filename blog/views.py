from PIL import Image

from django.shortcuts import render, redirect
from django.conf import settings

from .models import Post
from .forms import NewPostForm, ImageUploadForm

import os
import glob
import errno
from datetime import datetime


def index(request):
    latest_post_list = Post.objects.order_by('-travel_date')[:5]
    posts = Post.objects.order_by('-travel_date').all()
    if request.method == 'POST':
        post_author = request.user
        post = Post(author=post_author)
        form_data = NewPostForm(request.POST, instance=post)
        if form_data.is_valid():
            form_data.clean()
            form_data.save()
            return redirect('blog:index')
    post_form = NewPostForm()
    context = {'post_form': post_form,
               'latest_post_list': latest_post_list,
               'posts': posts,
               }
    template = 'blog/index.html'

    return render(request, template, context)


def gallery(request):
    if request.method == "POST" and request.user.is_authenticated:
        f = request.FILES["file"]
        _save_uploaded_image(f)

    images = _get_images_ending_with(".jpg") + _get_images_ending_with(".png")

    _generate_thumbnails(images)

    images = [i.replace(settings.MEDIA_ROOT, settings.MEDIA_URL, 1)
            for i in images]

    images = [(i.replace("markdownx", "thumbnails", 1), i)
            for i in images]

    context = {
            "images": images,
            "upload_form": ImageUploadForm(),
            }

    return render(request, 'blog/gallery.html', context)


def _get_images_ending_with(extension):
    return glob.glob(os.path.join(
        settings.MEDIA_ROOT, "markdownx", "*", "*", "*", "*" + extension))


def _save_uploaded_image(f):
    """
    Saves the uploaded file f in the designated folder.
    Creates this folder if necessary,
    """

    # First update timestamp for media
    settings.MARKDOWNX_MEDIA_PATH = datetime.now().strftime('/markdownx/%Y/%m/%d')

    full_name = os.path.join(settings.MEDIA_ROOT, settings.MARKDOWNX_MEDIA_PATH[1:], f.name)

    _make_path(full_name)

    with open(full_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def _generate_thumbnails(images):
    for img_path in images:
        thumb_path = img_path.replace("markdownx", "thumbnails", 1)

        if not os.path.isfile(thumb_path):
            img = Image.open(img_path)
            img.thumbnail((128, 128))
            _make_path(thumb_path)
            img.save(thumb_path)


def _make_path(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise 


