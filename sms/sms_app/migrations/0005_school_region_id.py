# Generated by Django 4.0.4 on 2022-05-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='region_id',
            field=models.IntegerField(default=100),
        ),
    ]
