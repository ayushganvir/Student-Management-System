# Generated by Django 4.0.3 on 2022-05-25 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0023_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='books',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
