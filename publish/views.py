from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render

# Create your views here.

def view_post(self):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post não existe")
    return render(request, 'post.html', context={'post': post})