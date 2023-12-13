from django.shortcuts import render,redirect
from .forms import PostForm,CommentForm
from .models import Post

def PnQ_home(request):
    list = Post.objects.all()
    return render(request,'PostsNQueries/PnQ_home.html',{'posts':list})
def create_post(request):
    if request.method=="POST":
        form  = PostForm(request.POST,request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.posted_by=request.user
            notice.save()
            return redirect('PostsNQueries:PnQ_home')
    else:
        form = PostForm
    return render(request, 'PostsNQueries/create_post.html',{'form':form})


def add_comment(request, post_serial):
    post = Post.objects.get(post_serial=post_serial)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commented_by = request.user
            comment.save()
    return redirect('PostsNQueries:PnQ_home') 

