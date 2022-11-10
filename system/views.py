from django.shortcuts import render, redirect
from .models import Students, Book, Book_Issue, Record_Issue
from datetime import date
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.


fine = 50


 
def error_404_view(request, exception):
    print("hcuierugheriuh")
    return render(request, 'system/404.html')

def index(request):
    return render(request, 'system/index.html')


def add_book(request):

    if request.method == "POST":
        

        if Book.objects.filter(book_title=request.POST.get('title')).exists() : 
            book = Book.objects.get(book_title=request.POST.get('title'))
            book.available = book.available + int(request.POST.get('total'))
            book.total = book.total + int(request.POST.get('total'))
            book.save(update_fields=["total","available"])
            return redirect('/books')


        Book.objects.create(
            book_title=request.POST.get('title'),
            book_author=request.POST.get('book_author'),
            book_pages=request.POST.get('book_pages'),
            summary=request.POST.get('summary'),
            available=request.POST.get('total'),
            total=request.POST.get('total')
        )
        return redirect('/books')
    else:
        return (render(request, 'system/add_book.html'))


def add_student(request):

    if request.method == "POST":
        Students.objects.create(
            prn=request.POST.get('prn'),
            name=request.POST.get('name'),
            branch=request.POST.get('branch'),
            email=request.POST.get('email')
        )
        return redirect('/students')
    else:
        return (render(request, 'system/add_student.html'))


def issue_book(request):

    if request.method == "POST":
        
        book_title=request.POST.get('book_title')
        prn = request.POST.get('prn')
        # prn = str(prn)
        # book_title = str(book_title)

        # print(prn)
        # print(book_title)

        if not Students.objects.filter(prn=prn).exists() or not Book.objects.filter(book_title=book_title).values().exists() : 
            print(Students.objects.filter(prn=prn))
            print(Book.objects.filter(book_title=book_title).values())
            return render(request, 'system/issue_book.html')



        student = Students.objects.get(prn=prn)
        book = Book.objects.get(book_title=book_title)


        book.available = book.available-1 
        book.save(update_fields=['available'])

        student.books_issued = student.books_issued+1 
        student.save(update_fields=['books_issued'])
        
        Book_Issue.objects.create(
            book_title=book_title,
            prn=prn
        )


        return redirect('/books_issued')
#     else:
#         context={'form':Book_IssueForm,"book":BookInstance.objects.filter(Is_borrowed=False)}
    return render(request, 'system/issue_book.html')


def students(request):
    students = Students.objects.all().values()
    return render(request, 'system/students.html', {'students': students})


def books(request):
    books = Book.objects.all().values()
    return render(request, 'system/books.html', {'books': books})


def books_issued(request):
    books_issued = Book_Issue.objects.all().values()
    return render(request, 'system/books_issued.html',{'books_issued':books_issued})

def records_issued(request):
    records_issued = Record_Issue.objects.all().values()
    return render(request, 'system/records_issued.html',{'records_issued':records_issued})

def delete_issue(request,id):
    issue = Book_Issue.objects.get(id=id)
    prn = issue.prn 
    book_title = issue.book_title

    student = Students.objects.get(prn=prn)
    book = Book.objects.get(book_title=book_title)


    due_date = str(issue.due_date)
    # print("due_date =", due_date)

    # today = datetime.date().today.strftime("%d/%m/%Y")
    today = str(date.today())
    # print("today =", today)

    # print(datetime.date().today())
    # print(issue.due_date)

    if today > due_date : 
        student.fine = student.fine + fine
        student.save(update_fields=['fine'])

    book.available = book.available+1 
    book.save(update_fields=['available'])

    student.books_issued = student.books_issued-1 
    student.save(update_fields=['books_issued'])

    Record_Issue.objects.create(
        prn = prn,
        book_title = book_title,
        issue_date = issue.issue_date,
    )



    issue.delete()
    return redirect('/books_issued')
