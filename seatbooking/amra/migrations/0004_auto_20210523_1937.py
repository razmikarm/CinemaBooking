# Generated by Django 3.2 on 2021-05-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amra', '0003_auto_20210523_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='seat_row_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='seats_in_row',
        ),
        migrations.AddField(
            model_name='theatre',
            name='seat_row_count',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theatre',
            name='seats_in_row',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
