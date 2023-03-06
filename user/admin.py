from django.contrib import admin

# Register your models here.
from .models import UserDetail
class UserDeatilAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'gender', 'birthdate', 'tel_num', 'roletype']
admin.site.register(UserDetail, UserDeatilAdmin)