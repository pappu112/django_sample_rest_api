# Generated by Django 4.0.4 on 2022-06-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='extra_data',
            field=models.TextField(null=True),
        ),
    ]