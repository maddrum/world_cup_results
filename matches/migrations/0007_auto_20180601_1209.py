# Generated by Django 2.0.2 on 2018-06-01 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_auto_20180601_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='country_home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_home', to='matches.Countries'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='match_state',
            field=models.CharField(blank=True, choices=[('home', 'Победа домакин'), ('guest', 'Победа гост'), ('tie', 'Равен')], max_length=20),
        ),
    ]
