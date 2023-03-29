from django.shortcuts import render
from blog.forms import *
from blog.models import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.core.exceptions import PermissionDenied

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

class PostCreate(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'post_form.html'
    success_url = '/pages/'
    fields = ['title', 'subtitle', 'body', 'date', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    success_url = '/pages/'
    template_name = 'post_form.html'
    fields = ['title', 'subtitle', 'body']
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/pages/'
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
