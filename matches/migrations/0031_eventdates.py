# Generated by Django 2.0.2 on 2018-07-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0030_auto_20180629_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
            ],
        ),
    ]
