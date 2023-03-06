from django.contrib import admin

# Register your models here.
from .models import course,usercourse
class courseAdmin(admin.ModelAdmin):
    list_display = ['room_id', 'course_name', 'course_describe', 'created_on', 'updated_on', 'user']

admin.site.register(course, courseAdmin)
admin.site.register(usercourse)
