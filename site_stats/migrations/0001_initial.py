# Generated by Django 2.0.2 on 2018-07-04 10:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_predictions', models.IntegerField()),
                ('total_points_gained', models.IntegerField()),
                ('total_match_states_guessed', models.IntegerField()),
                ('total_match_results_guessed', models.IntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('user_guessed_most_match_states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats_user_match_states', to=settings.AUTH_USER_MODEL)),
                ('user_guessed_most_results', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats_user_results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
