# Generated by Django 4.0.2 on 2022-10-01 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_alter_book_issue_due_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fine',
        ),
        migrations.AddField(
            model_name='students',
            name='fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 9, 38, 5, 671974), help_text='Date the book is due to'),
        ),
    ]