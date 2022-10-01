# Generated by Django 4.0.2 on 2022-10-01 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_fine_remove_book_issue_book_instance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 9, 18, 2, 496706), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='issue_date',
            field=models.DateField(auto_now=True, help_text='Date the book is issued'),
        ),
        migrations.AlterField(
            model_name='students',
            name='prn',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
