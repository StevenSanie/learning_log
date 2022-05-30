from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Topic, Entry

# Create your views here.
def index(request):
	return render(request, 'learning_logs/index.html')

class TopicsList(generic.ListView):
	model = Topic
	template_name = 'learning_logs/topics.html'
	paginate_by = 5


class AddTopic(generic.CreateView):
	model = Topic
	template_name = 'learning_logs/add-topic.html'
	fields = ['topic_name']
	success_url = reverse_lazy('topics')

class DeleteTopic(generic.DeleteView):
	model = Topic
	success_url = reverse_lazy('topics')

class EditTopic(generic.UpdateView):
	model = Topic
	success_url = reverse_lazy('topics')
	fields = ['topic_name']
	template_name = 'learning_logs/edit_topic.html'

class DetailTopic(generic.DetailView):
	model = Topic
	template_name = 'learning_logs/topic-detail.html'
