from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
	path('register', views.registerUser, name='register'),
	path('', views.index, name='index'),
	path("topics/", views.TopicsList.as_view(), name="topics"),
	path('topic/new', views.add_topic, name='add-topic'),
	path('topics/<int:pk>/delete/', views.DeleteTopic.as_view(), name='delete-topic'),
	path('topics/<int:pk>/update/', views.EditTopic.as_view(), name='update-topic'),
	path('topics/<int:pk>/', views.DetailTopic.as_view(), name='topic-detail'),
	path('entry/<int:topic_id>', views.new_entry, name='new-entry'),
	path('entry/edit/<int:pk>/', views.EditEntry.as_view(), name='edit-entry'),
	path('entry/delete/<int:pk>/', views.DeleteEntry.as_view(), name='delete-entry'),
]
