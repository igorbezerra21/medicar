# Generated by Django 2.2.9 on 2021-10-11 02:15

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20211010_2044'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='consultas',
            unique_together={('dia', 'horario', 'usuario')},
        ),
        migrations.AddConstraint(
            model_name='agenda',
            constraint=models.CheckConstraint(check=models.Q(dia__gte=datetime.datetime(2021, 10, 11, 2, 15, 3, 102040, tzinfo=utc)), name='dia__gte'),
        ),
    ]
