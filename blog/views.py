from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404


# Create your views here.

from .models import Blog, Comments, Profile
from django.views import generic

def index(request):
    num_blogs=Blog.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    bloggercount=Profile.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_blogs':num_blogs, 'bloggercount':bloggercount},
    )

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class ProfileListView(generic.ListView):
    model = Profile

class ProfileDetailView(generic.DetailView):
    model = Profile

class CommentCreate(CreateView):
    model = Comments
    fields = ['description']
    