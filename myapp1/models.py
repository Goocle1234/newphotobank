from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=50, default='none')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(Topic, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image of {self.title.title}"