# Generated by Django 2.0.2 on 2018-06-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus_points', '0006_auto_20180618_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusdescription',
            name='available_choices',
            field=models.CharField(default='No', max_length=600),
        ),
        migrations.AlterField(
            model_name='bonusdescription',
            name='input_filed',
            field=models.CharField(choices=[('text', 'text'), ('number', 'number'), ('all-countries', 'all-countries'), ('choices', 'choices')], default='text', max_length=20),
        ),
    ]
