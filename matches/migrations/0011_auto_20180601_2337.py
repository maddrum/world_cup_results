# Generated by Django 2.0.2 on 2018-06-01 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0010_auto_20180601_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPredictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_match_state', models.CharField(choices=[('home', 'Победа домакин'), ('guest', 'Победа гост'), ('tie', 'Равен')], max_length=20)),
                ('prediction_goals_home', models.IntegerField()),
                ('prediction_goals_guest', models.IntegerField()),
                ('user_points', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='matches',
            unique_together={('country_home', 'country_guest', 'phase')},
        ),
        migrations.AddField(
            model_name='userpredictions',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_predictions', to='matches.Matches'),
        ),
        migrations.AddField(
            model_name='userpredictions',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
