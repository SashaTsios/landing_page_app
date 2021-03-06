# Generated by Django 3.0.2 on 2020-01-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200116_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name_s', models.CharField(max_length=50)),
                ('bot_name_s', models.CharField(max_length=50)),
                ('description_s', models.TextField(max_length=500)),
                ('is_active_s', models.BooleanField(default=False)),
            ],
        ),
    ]
