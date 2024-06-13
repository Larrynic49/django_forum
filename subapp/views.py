from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Post


# Create your views here.
def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
             # if the form is valid
        if form.is_valid():
              # Yes, Save
            form.save()

              # Redirect to Home
            return HttpResponseRedirect('/')
    
        else:
           # No, Show Error
            return HttpResponseRedirect(form.error.as_json())
    
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'post.html',
                  {'posts': posts})


def delete(request, post_id):
    #find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, "edit.html", {'post': post})


def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes+1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')