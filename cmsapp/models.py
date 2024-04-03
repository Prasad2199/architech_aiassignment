from django.db import models

# Create your models here.
from django.db import models
from authentication.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ContentItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/')
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
