from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

from .models import Blog, Comments, Profile
from django.views import generic

def index(request):
    num_blogs=Blog.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    num_bloggers=User.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_blogs':num_blogs},
    )

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class ProfileListView(generic.ListView):
    model = Profile

