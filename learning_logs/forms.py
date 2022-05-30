from dataclasses import fields
from django.forms import ModelForm

class TopicForm(ModelForm):
	class Meta:
		fields = ['topic_name']
		