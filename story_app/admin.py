from django.contrib import admin
from .models import Story
from mptt.admin import DraggableMPTTAdmin

class StoryInline(admin.TabularInline):
    model = Story
    fk_name = 'parent'
    extra = 2

@admin.register(Story)
class FamilyAdmin(DraggableMPTTAdmin):
    inlines = [StoryInline]
    list_display = ['tree_actions', 'indented_title','title', 'parent']
    list_display_links = ('indented_title', 'title')