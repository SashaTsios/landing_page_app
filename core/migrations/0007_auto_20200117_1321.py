# Generated by Django 3.0.2 on 2020-01-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description_s',
            field=models.TextField(max_length=1000),
        ),
    ]
