# Generated by Django 2.2.9 on 2021-10-20 00:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211019_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.RemoveConstraint(
            model_name='agenda',
            name='dia__gte',
        ),
        migrations.AddConstraint(
            model_name='agenda',
            constraint=models.CheckConstraint(check=models.Q(dia__gte=datetime.datetime(2021, 10, 20, 0, 5, 2, 897461, tzinfo=utc)), name='dia__gte'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
