from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


def index(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
                        Q(title__contains=query)|
                        Q(content__contains=query)
                        ).distinct()
    paginator = Paginator(posts_list, 3)  # Show 3 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'posts' : posts})


def detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,'detail.html',{'post':post})


def new_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.title = form.cleaned_data['title']
        post.save()
        messages.success(request,"New Post Created")
        return redirect('main:detail',post.slug)
    else:
        messages.error(request,"Problem Creating Post")
    return render(request,'post_form.html',{'form' : form})


def update_post(request,slug):
    instance = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        post = form.save(commit=False)
        post.title = form.cleaned_data['title']
        post.save()
        messages.success(request,"Sucessfully Updated")
        return redirect('main:detail', post.slug)
    else:
        messages.error(request, "Update Failed")
    return render(request, 'post_form.html', {'form': form})


def delete_post(request,slug):
    instance = Post.objects.get(slug=slug)
    instance.delete()
    messages.success(request,"Deletion Successfull")
    return redirect('main:index')