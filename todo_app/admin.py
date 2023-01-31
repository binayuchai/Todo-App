from django.contrib import admin
from todo_app.models import TODO
# Register your models here.
@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ("title","created_at")
    search_fields = ("title",)
    
    