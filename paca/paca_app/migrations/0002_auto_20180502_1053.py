# Generated by Django 2.0.2 on 2018-05-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paca_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='manager',
            field=models.ManyToManyField(to='paca_app.Manager'),
        ),
    ]
