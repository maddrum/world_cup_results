# Generated by Django 2.0.2 on 2018-06-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0027_matches_penalties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='match_state',
            field=models.CharField(blank=True, choices=[('home', 'Победа домакин'), ('guest', 'Победа гост'), ('tie', 'Равен'), ('penalties_home', 'Победа за домакин след дузпи'), ('penalties_guest', 'Победа за гост след дузпи')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userpredictions',
            name='prediction_match_state',
            field=models.CharField(choices=[('home', 'Победа домакин'), ('guest', 'Победа гост'), ('tie', 'Равен'), ('penalties_home', 'Победа за домакин след дузпи'), ('penalties_guest', 'Победа за гост след дузпи')], max_length=20),
        ),
    ]