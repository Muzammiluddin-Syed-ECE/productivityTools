from django.urls import path
from . import views
app_name = 'notetaking'
urlpatterns = [
    path('<int:subject_id>/', views.chapters, name='chapters'),
    path('<int:subject_id>/<int:chapter_id>', views.topics, name='topics'),
    path('<int:subject_id>/<int:chapter_id>/<int:topic_id>', views.definitions, name='definitions'),
    path('creating/', views.new_subject, name='new_subject'),
    path('<int:subject_id>/creating/', views.new_chapter, name='new_chapter'),
    path('<int:subject_id>/<int:chapter_id>/creating/', views.new_topic, name='new_topic'),
    path('<int:subject_id>/<int:chapter_id>/<int:topic_id>/creating/', views.new_definition, name='new_definition'),
    path('delete/', views.delete_subject, name='delete_subject'),
    path('<int:subject_id>/delete/', views.delete_chapter, name='delete_chapter'),
    path('<int:subject_id>/<int:chapter_id>/delete/', views.delete_topic, name='delete_topic'),
    path('<int:subject_id>/<int:chapter_id>/<int:topic_id>/delete/', views.delete_definition, name='delete_definition'),
    path('', views.index, name='index'),
]
