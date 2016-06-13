from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    folder = models.ForeignKey('Folder')
    text = models.TextField(null=True, blank=True)
    pathname = models.CharField(max_length=1024, null=True, blank=True)
    created_on = models.DateTimeField(null=False, blank=False, default=timezone.now)
    def __str__(self):
        return self.title

class Folder(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)    
    parent = models.ForeignKey('Folder', null=False)

    def __str__(self):
        return self.name
    
