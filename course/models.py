from django.db import models
from user.models import UserDetail
from django.utils import timezone
# Create your models here.
class course(models.Model):
    room_id = models.AutoField(verbose_name="房间号", primary_key=True)
    course_name = models.CharField(max_length=50, null=True, blank=True)
    course_describe = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_created=True,default=timezone.now())
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(UserDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class usercourse(models.Model):
    room_id = models.BigIntegerField(max_length=50, null=True, blank=True)
    user_id = models.BigIntegerField(max_length=50, null=True, blank=True)
