# Generated by Django 5.0.7 on 2024-07-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userhobbies_customuser_smoking_habits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='hobbies',
            field=models.ManyToManyField(blank=True, related_name='user_hobbies', to='users.userhobbies'),
        ),
    ]