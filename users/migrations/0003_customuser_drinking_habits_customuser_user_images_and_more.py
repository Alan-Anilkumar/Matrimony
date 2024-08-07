# Generated by Django 5.0.7 on 2024-07-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_short_reel_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='drinking_habits',
            field=models.CharField(choices=[('NON-ALCOHOLIC', 'Non Alcoholic'), ('OCCASIONALLY', 'Occasionally'), ('REGULAR', 'Regular'), ('WANTING TO QUIT', 'Wanting To Quit')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_images',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]
