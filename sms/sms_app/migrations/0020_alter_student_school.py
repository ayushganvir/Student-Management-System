# Generated by Django 4.0.3 on 2022-05-25 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0019_rename_book_student_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sms_app.school'),
        ),
    ]