# Generated by Django 2.0.2 on 2018-06-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20180601_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='match_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
