from django.db import models
from datetime import datetime,timedelta
import uuid

class Students(models.Model):
    prn = models.CharField(unique=True,max_length=100)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    fine = models.IntegerField(default=0)
    books_issued = models.IntegerField(default=0)

    def __str__(self):
        return self.prn

class Book(models.Model):
    book_title = models.CharField(unique=True,max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.PositiveIntegerField()
    summary=models.TextField(max_length=500, help_text="Summary about the book",null=True,blank=True)
    available = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return self.book_title

def get_returndate():
    return datetime.today() + timedelta(days=8)

class Book_Issue(models.Model):
    prn = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    issue_date = models.DateField(auto_now=True,help_text="Date the book is issued")
    due_date = models.DateField(default=get_returndate(),help_text="Date the book is due to")
    
    def __str__(self):
        return self.prn + " borrowed " + self.book_title

class Record_Issue(models.Model):
    prn = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    issue_date = models.DateField(null=True, blank=True,help_text="Date the book is issued")
    date_returned=models.DateField(auto_now=True,help_text="Date the book is returned")
    
    def __str__(self):
        return self.prn + " borrowed " + self.book_title