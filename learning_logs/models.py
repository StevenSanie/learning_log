from tabnanny import verbose
from django.db import models
from django.forms import NullBooleanField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""Models to represent a topic"""
	topic_name = models.CharField(max_length=60)
	date_added = models.DateTimeField(auto_now_add=True)
	topic_description = models.TextField(max_length=80, blank=True, null=True)
	topic_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	class Meta:
		ordering = ['-date_added']

	def get_absolute_url(self):
		return reverse("topic-detail", kwargs={"pk": self.pk})
	

	def __str__(self):
		return self.topic_name


class Entry(models.Model):
	entry_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	entry_title = models.CharField(max_length=100, blank=True)
	entry_text = models.TextField(max_length=500)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'
		ordering = ['-date_added']

	def __str__(self):
		return f"{self.entry_title} - {self.entry_topic}"

