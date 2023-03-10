# Generated by Django 4.1.5 on 2023-01-30 23:21

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
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle_worked', models.CharField(max_length=64)),
                ('exercise_name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('sets', models.IntegerField(help_text='enter number')),
                ('reps', models.IntegerField(help_text='enter number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_ate', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
