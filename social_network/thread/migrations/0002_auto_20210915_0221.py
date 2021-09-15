# Generated by Django 3.1.2 on 2021-09-14 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_message', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='thread',
            name='archive',
        ),
        migrations.AddField(
            model_name='thread',
            name='archive',
            field=models.ManyToManyField(related_name='archive', to=settings.AUTH_USER_MODEL),
        ),
    ]
