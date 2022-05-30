from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.
class Topic(models.Model):
	"""Models to represent a topic"""
	topic_name = models.CharField(max_length=60)
	date_added = models.DateTimeField(auto_now_add=True)


	def get_absolute_url(self):
		return reverse("topic-detail", kwargs={"pk": self.pk})
	

	def __str__(self):
		return self.topic_name


class Entry(models.Model):
	entry_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, help_text='Select Topic')
	entry_title = models.CharField(max_length=100, help_text='Entry title', blank=True)
	entry_text = models.TextField(max_length=500, help_text='Enter your entry')
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return f"{self.entry_title} - {self.entry_topic}"

