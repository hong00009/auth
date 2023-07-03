from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.decorators.http import require_POST

# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #DB에 아직 저장하지 않고(commit False) post변수에 임시저장
            post.user = request.user
            post.save()

            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form' : form,
    }

    return render(request, 'posts/form.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()

    context = {
        'post' : post,
        'form' : form,
    }

    return render(request, 'posts/detail.html', context)

@require_POST
@login_required
def comments_create(request, id):
    post = Post.objects.get(id=id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

        return redirect('posts:detail', id)