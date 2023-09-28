from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post, Group
from .forms import *

User = get_user_model()

def profile(request, username):
    template = 'posts/profile.html'
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-pub_date')[:10]
    count_posts = posts.count()    
    context = {
        'count_posts': count_posts,
        'user': user,
        'posts': posts
    }
    return render(request, template, context)
    
    
def post_detail(request, post_id):
    template = 'posts/posts.html'
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, template, context)


def index(request):
    template = 'posts/index.html'
    posts_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': "Главная страница",
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': "Здесь информация о мороженном}",
        'posts': posts,
        'group': group
    }
    return render(request, template, context)

@login_required
def add_post(request):
    template = 'posts/add_post.html'
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('posts:profile', args=[request.user.username]))
    else:
        form = CreatePost()
    context = {
        'form': form,
    }
    return render(request, template, context)