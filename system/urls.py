from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('add_book/', views.add_book,name='add_book'),
    path('add_student/', views.add_student,name='add_student'),
    path('issue_book/', views.issue_book,name='issue_book'),
    path('students/', views.students,name='students'),
    path('books/', views.books,name='books'),
    path('books_issued/', views.books_issued,name='books_issued'),
    path('records_issued/', views.records_issued,name='records_issued'),
    path('delete_issue/<id>', views.delete_issue,name='delete_issue'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
