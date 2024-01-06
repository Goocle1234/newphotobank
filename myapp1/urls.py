from django.urls import path

from .views import text, categories, upload_image, display_photos, create_topic

app_name = 'myapp1'
urlpatterns = [
    path('create_topic', create_topic, name='create_topic'),
    path('', text, name='text'),
    path('categories/', categories, name='categories'),
    path('upload/', upload_image, name='upload_image'),
    path('photos/<int:topic_id>/', display_photos, name='display_photos'),
]