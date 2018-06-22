from django.shortcuts import render
from django.conf import settings

from .models import Post
from .forms import NewPostForm, ImageUploadForm

import os
import glob
import errno
from datetime import datetime


def index(request):
    latest_post_list = Post.objects.order_by('-travel_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)


def gallery(request):
    if request.method == "POST":
        f = request.FILES["file"]
        _save_uploaded_image(f)

    images = _get_images_ending_with(".jpg") + _get_images_ending_with(".png")
    images = [i.replace(settings.MEDIA_ROOT, settings.MEDIA_URL, 1) for i in images]
    context = {
            "images": images,
            "upload_form": ImageUploadForm(),
            }
    return render(request, 'blog/gallery.html', context)


def _get_images_ending_with(extension):
    return glob.glob( os.path.join(settings.MEDIA_ROOT, "markdownx", "*", "*", "*", "*" + extension ) )


def _save_uploaded_image(f):
    """ 
    Saves the uploaded file f in the designated folder. 
    Creates this folder if necessary,
    """

    # First update timestamp for media
    settings.MARKDOWNX_MEDIA_PATH = datetime.now().strftime('/markdownx/%Y/%m/%d')
    full_name = os.path.join(settings.MEDIA_ROOT, settings.MARKDOWNX_MEDIA_PATH[1:], f.name)

    if not os.path.exists(os.path.dirname(full_name)):
        try:
            os.makedirs(os.path.dirname(full_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(full_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def new(request):
    post_form = NewPostForm()
    context = {'post_form': post_form}
    template = 'blog/new.html'
    return render(request, template, context)
