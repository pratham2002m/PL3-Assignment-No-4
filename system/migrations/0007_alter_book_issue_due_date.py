# Generated by Django 4.0.2 on 2022-10-01 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_students_books_issued_alter_book_issue_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 9, 36, 48, 958796), help_text='Date the book is due to'),
        ),
    ]
