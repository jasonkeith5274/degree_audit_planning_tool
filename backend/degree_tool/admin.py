from django.contrib import admin
from .models import LevelingCourse

class LevelingCourseAdmin(admin.ModelAdmin):
    display = ('class_num')

# Register your models here.
admin.site.register(LevelingCourse, LevelingCourseAdmin)