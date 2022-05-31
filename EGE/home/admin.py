from django.contrib import admin
from .models import typeTask, Task, subType
@admin.register(subType)
class SubtypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type')
    list_display_links = (None)
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Task)
admin.site.register(typeTask)