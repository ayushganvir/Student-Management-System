# Generated by Django 4.0.4 on 2022-05-26 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0027_remove_student_books_remove_student_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
