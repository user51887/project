
from .models import Post , Comment
from .forms import CommentForm
from django.shortcuts import render
from django.db.models import Q
# Create your views here.


def post_list(request):
    post_list = Post.objects.all()

    ## search 
    search_query = request.GET.get('q')
    if search_query :
        post_list = post_list.filter(
            Q(title__icontains = search_query)|
            Q(content__icontains= search_query) |
            Q(tags__name__icontains= search_query)
        ).distinct()

    

    
    context = {
        'post_list' : post_list ,
    }

    return render(request , 'Post/post_list.html' , context)


def post_detail(request , id):
    post_detail = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post_detail)
    

    if request.method == 'POST' :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'post_detail' : post_detail ,
        'comments' : comments ,
        'comment_form' : comment_form
    }

    return render(request , 'Post/post_detail.html' , context)














