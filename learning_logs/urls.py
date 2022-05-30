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
]
