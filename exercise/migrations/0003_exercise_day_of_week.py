# Generated by Django 4.1.5 on 2023-01-30 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_exercise_weight_alter_exercise_reps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='day_of_week',
            field=models.DateField(auto_now=True),
        ),
    ]
