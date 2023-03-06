from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#引入auth_user表
    # nickname = models.CharField(_("nickname"), max_length=30, null=True, blank=True)#昵称
    nickname = models.CharField(_("nickname"), max_length=30, null=True, blank=True)  # 昵称
    GENDER_CHOICES = (
        ('Male', _('Male')),
        ('Female', _('Female')),#懒翻译字符串
    ) #choice
    # gender = models.CharField(_("gender"), max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=30,  null=True, blank=True)
    birthdate = models.DateField(_("birthdate"), blank=True, null=True)
    tel_num = models.CharField(_("PhoneNumber"), max_length=30, null=True, blank=True)
    roletype = models.CharField(_("roletype"), max_length=30, default=2)

    def __str__(self):
        return self.user.username
