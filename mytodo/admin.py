from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TakAdmin(admin.ModelAdmin):
    list_display = ('user','title','complete','created','updated')

    list_filter = ('complete',)

# admin.site.register(Task)