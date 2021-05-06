# Generated by Django 3.2 on 2021-05-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_action', models.CharField(max_length=30)),
                ('activity_date', models.DateField(verbose_name='date published')),
                ('search_value', models.CharField(max_length=30)),
            ],
        ),
    ]