from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Topic, Image
from .forms import ImageUploadForm, TopicForm


def text(request):
    return render(request, 'myapp1/index.html')

@login_required
def categories(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'myapp1/categories.html', context)

@login_required
def upload_image(request):
    if request.method != 'POST':
        form = ImageUploadForm()
    else:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp1:categories')
    context = {'form': form}
    return render(request, 'myapp1/upload_image.html', context)



def display_photos(request, topic_id):
    # Получаем объект темы по ID
    topic = Topic.objects.get(pk=topic_id)
    # Фильтруем изображения, связанные с этой темой
    images = Image.objects.filter(title=topic)
    context = {'topics_with_images': images}
    return render(request, 'myapp1/display_photos.html', context)

@login_required
def create_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.title = form.cleaned_data['title'].capitalize()  # Преобразование текста
            topic.save()
            return redirect('myapp1:categories')

    context = {'form': form}
    return render(request, 'myapp1/create_topic.html', context)