from django.shortcuts import render, get_object_or_404
from django.dispatch import receiver
from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from itertools import groupby

# Create your views here.

class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    success_url = "/message/"
    template_name = 'message_form.html'
    fields = ['reciever', 'content']
    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.date = datetime.now()
        return super().form_valid(form)

class MessageList(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = Message.objects.filter(reciever=self.request.user)
        messages_by_author = groupby(messages.order_by('sender', '-date'), lambda message: message.sender)
        authors = [{'author': author, 'messages': list(messages)} for author, messages in messages_by_author]
        context['authors'] = authors
        return context

class MessageDetail(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'message_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        autor = get_object_or_404(User, id=self.object.sender.id)
        context['autor'] = autor
        return context