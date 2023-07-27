# Generated by Django 4.2.3 on 2023-07-26 06:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2023, 7, 26, 11, 47, 14, 865897))),
                ('designation', models.TextField(max_length=30)),
                ('city', models.TextField(max_length=20)),
                ('state', models.TextField(max_length=20)),
                ('country', models.TextField(max_length=20)),
                ('isTrending', models.BooleanField(default=False)),
                ('min_exp', models.IntegerField(default=0)),
                ('max_exp', models.IntegerField(default=0)),
                ('starred', models.BooleanField(default=False)),
                ('assigned_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_by', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
