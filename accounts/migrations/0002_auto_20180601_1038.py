# Generated by Django 2.0.2 on 2018-06-01 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userqueries',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='UserQueries',
        ),
    ]
