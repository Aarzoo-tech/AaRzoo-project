# Generated by Django 3.2.6 on 2021-09-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_contest',
            name='ans',
            field=models.CharField(default='', max_length=50),
        ),
    ]