from cProfile import label
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Topic, Entry

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = [
			'topic_name',
			'topic_description',
		]
		
		labels = {
			'topic_name': 'Name',
			'topic_description': 'Description'
		}

class EntryForm(ModelForm):
	class Meta:
		model = Entry
		fields = ['entry_title', 'entry_text']
		labels = {
			'entry_title': 'Heading',
			'entry_text': 'Entry'
		}