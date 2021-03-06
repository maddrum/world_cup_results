# Generated by Django 2.0.2 on 2018-06-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0020_userpredictions_gave_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpredictions',
            name='points_gained',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userpredictions',
            name='prediction_note',
            field=models.TextField(default='Дал си прогноза за мача: 1 т.\\n'),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='prediction_goals_guest',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='prediction_goals_home',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
