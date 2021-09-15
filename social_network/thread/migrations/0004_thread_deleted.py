# Generated by Django 3.1.2 on 2021-09-14 22:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thread', '0003_auto_20210915_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='deleted',
            field=models.ManyToManyField(related_name='deleted', to=settings.AUTH_USER_MODEL),
        ),
    ]
