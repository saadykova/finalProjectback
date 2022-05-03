from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

# Register your models here.
