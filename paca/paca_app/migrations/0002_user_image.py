# Generated by Django 2.0.4 on 2018-05-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paca_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]