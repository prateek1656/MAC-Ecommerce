from math import fabs
from django.shortcuts import render, HttpResponse

from .models import Blogpost

def index(request):
    allblogs = Blogpost.objects.all()
    params = {'allblogs':allblogs}
    return render(request,'blogs/index.html',params)

def blogpost(request,post_id):
    blog = Blogpost.objects.filter(post_id = post_id)
    if Blogpost.objects.filter(post_id = post_id +1):
        next_blog_id = post_id + 1
        next_able = "enabled"
    else:
        next_blog_id = post_id
        next_able = "disabled"
    prev_blog_id = post_id - 1
    if Blogpost.objects.filter(post_id = post_id -1):
        prev_blog_id = post_id - 1
        prev_able = "enabled"
    else:
        prev_blog_id = post_id
        prev_able = "disabled"
    return render(request,'blogs/blogpost.html',{'blog':blog[0],'next_blog':next_blog_id,'prev_blog':prev_blog_id,'next_able':next_able,'prev_able':prev_able})



