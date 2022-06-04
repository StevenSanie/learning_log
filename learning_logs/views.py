from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Topic, Entry
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
def index(request):
	entries = Entry.objects.all()
	entry_count = Entry.objects.count
	context = {
		'entries': entries,
		'entry_count': entry_count
	}
	return render(request, 'learning_logs/index.html', context)

class TopicsList(LoginRequiredMixin, generic.ListView):
	model = Topic
	template_name = 'learning_logs/topics.html'
	paginate_by = 5


class AddTopic(LoginRequiredMixin, generic.CreateView):
	model = Topic
	template_name = 'learning_logs/add-topic.html'
	fields = ['topic_name']
	success_url = reverse_lazy('topics')

class DeleteTopic(LoginRequiredMixin, generic.DeleteView):
	model = Topic
	success_url = reverse_lazy('topics')

class EditTopic(LoginRequiredMixin, generic.UpdateView):
	model = Topic
	success_url = reverse_lazy('topics')
	fields = ['topic_name']
	template_name = 'learning_logs/edit_topic.html'

class DetailTopic(LoginRequiredMixin, generic.DetailView):
	model = Topic
	template_name = 'learning_logs/topic-detail.html'


# Entry Views
class CreateEntry(LoginRequiredMixin, generic.CreateView):
	model = Entry
	template_name = 'learning_logs/create_entry.html'
	fields = '__all__'
	success_url = reverse_lazy('index')

class Entries(LoginRequiredMixin, generic.ListView):
	model = Entry
	template_name = 'learning_logs/entries.html'

class DetailEntry(LoginRequiredMixin, generic.DetailView):
	model = Entry
	template_name = 'learning_logs/detail-entry.html'
	
class EditEntry(LoginRequiredMixin, generic.UpdateView):
	model = Entry
	fields = '__all__'
	template_name = 'learning_logs/edit-entry.html'
	success_url = reverse_lazy('entries')


class DeleteEntry(LoginRequiredMixin, generic.DeleteView):
	model = Entry
	template_name = 'learning_logs/delete-entry.html'
	success_url = reverse_lazy('entries')