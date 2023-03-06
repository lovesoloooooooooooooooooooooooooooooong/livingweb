# Generated by Django 3.2.7 on 2022-01-28 09:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('course', '0003_auto_20220124_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 1, 28, 9, 20, 16, 390131, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='usercourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.ManyToManyField(to='course.course')),
                ('user_id', models.ManyToManyField(to='user.UserDetail')),
            ],
        ),
    ]