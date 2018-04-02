from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .forms import NewCommentForm
from django.shortcuts import redirect
# Create your views here.

from .models import Blog, Comments, Profile
from django.views import generic

def index(request):
    num_blogs=Blog.objects.all().count()
    num_comments=Comments.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    bloggercount=Profile.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_blogs':num_blogs, 'bloggercount':bloggercount, 'num_comments':num_comments},
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


def add_comment_to_post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.blog = blog
            comments.commenter = request.user
            comments.save()
            return redirect('blog-detail', pk=blog.pk)
    else:
        form = NewCommentForm()
    return render(request, 'blog/comments_form.html', {'form': form})