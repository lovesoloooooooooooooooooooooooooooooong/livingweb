# Generated by Django 3.2.7 on 2022-01-24 04:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('course', '0002_auto_20220121_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 1, 24, 4, 23, 12, 844911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='room_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='房间号'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.userdetail'),
        ),
    ]
