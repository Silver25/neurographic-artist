from django.shortcuts import render
# from django.http import HttpResponse  DEL
from django.views import generic
from .models import Post

# Create your views here.

# def journal(request):   DEL
#     return HttpResponse("This is Journal page")
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"