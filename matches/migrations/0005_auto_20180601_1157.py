# Generated by Django 2.0.2 on 2018-06-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_auto_20180601_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='match_state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='matches',
            name='score_guest',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='score_home',
            field=models.IntegerField(blank=True),
        ),
    ]
