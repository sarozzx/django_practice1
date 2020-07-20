from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Blogs

def index(request):

    latest_blogs_list = Blogs.objects.all()
    template=loader.get_template('blog/index.html')
    context={
        'latest_blogs_list':latest_blogs_list
    }

    return HttpResponse(template.render(context,request))

def detail(request, Blogs_id):

    return HttpResponse("You're looking at blog %s." % Blogs_id)

def author_name(request, Blogs_id):
    response = "You're looking at the author of blog %s."
    return HttpResponse(response % Blogs_id)



