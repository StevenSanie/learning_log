from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
	entries = Entry.objects.all()
	entry_count = Entry.objects.count
	context = {
		'entries': entries,
		'entry_count': entry_count
	}
	return render(request, 'learning_logs/index.html', context)

def registerUser(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False) 
			user.username = user.username.lower()
			user.save()
			login(request, user)
			return redirect('index')

	context = {
		'form': form
	}
	return render(request, 'registration/register.html', context)

class TopicsList(LoginRequiredMixin, generic.ListView):
	model = Topic
	template_name = 'learning_logs/topics.html'
	paginate_by = 5

	def get_queryset(self):
		topic_host = Topic.objects.filter(owner=self.request.user)
		return topic_host


@login_required
def add_topic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.owner = request.user
			topic.save()
			return redirect('topics')

	context = {
		'form': form
	}
	return render(request, 'learning_logs/add-topic.html', context)

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
@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.topic = topic
			entry.save()
			return redirect('topic-detail', topic_id)
		
	context = {
		'form': form,
		'topic': topic,
	}

	return render(request, 'learning_logs/create_entry.html', context)

class EditEntry(LoginRequiredMixin, generic.UpdateView):
	model = Entry
	fields = ['entry_title', 'entry_text']
	template_name = 'learning_logs/edit-entry.html'
	success_url = reverse_lazy('topics')


class DeleteEntry(LoginRequiredMixin, generic.DeleteView):
	model = Entry
	template_name = 'learning_logs/delete-entry.html'
	success_url = reverse_lazy('topics')