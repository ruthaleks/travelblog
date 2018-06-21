from django.shortcuts import render

from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-travel_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)


def gallery(request):
    raise NotImplementedError()


def new(request):
    raise NotImplementedError()
