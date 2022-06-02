from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path("topics/", views.TopicsList.as_view(), name="topics"),
	path('topics/new', views.AddTopic.as_view(), name='add-topic'),
	path('topics/<int:pk>/delete/', views.DeleteTopic.as_view(), name='delete-topic'),
	path('topics/<int:pk>/update/', views.EditTopic.as_view(), name='update-topic'),
	path('topics/<int:pk>/', views.DetailTopic.as_view(), name='topic-detail'),
	path('entry/new/', views.CreateEntry.as_view(), name='new-entry'),
	path('entries/', views.Entries.as_view(), name='entries'),
	path('entry/<int:pk>/', views.DetailEntry.as_view(), name='entry-detail'),
	path('entry/edit/<int:pk>/', views.EditEntry.as_view(), name='edit-entry'),
	path('entry/delete/<int:pk>/', views.DeleteEntry.as_view(), name='delete-entry'),
]
