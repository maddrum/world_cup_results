# Generated by Django 2.0.2 on 2018-06-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus_points', '0003_bonusdescription_input_filed'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusdescription',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]