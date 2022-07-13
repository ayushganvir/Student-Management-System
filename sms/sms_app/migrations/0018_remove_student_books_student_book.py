# Generated by Django 4.0.3 on 2022-05-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0017_rename_book_student_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='books',
        ),
        migrations.AddField(
            model_name='student',
            name='book',
            field=models.ManyToManyField(blank=True, to='sms_app.book'),
        ),
    ]
