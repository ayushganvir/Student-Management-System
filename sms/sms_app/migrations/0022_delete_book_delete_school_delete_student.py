# Generated by Django 4.0.3 on 2022-05-25 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0021_remove_student_books_remove_student_email_and_more'),
    ]

    operations = [
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