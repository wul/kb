from django.contrib import admin
from kb import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'folder', 'pathname']
    list_filter = ('folder',)



admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Folder)

