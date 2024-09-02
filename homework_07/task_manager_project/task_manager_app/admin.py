from django.contrib import admin

from .models import Task, Tag


class TagTabularInline(admin.TabularInline):
    model = Task.tags.through


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [
        TagTabularInline,
    ]
    list_display = ['pk', 'title', 'published_at']
    list_display_links = ['pk', 'title']


class TaskTabularInline(admin.TabularInline):
    model = Tag.tasks.through


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [
        TaskTabularInline,
    ]
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
