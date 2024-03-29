from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('courses/', views.courses, name='courses'),
    path('courses/details/<int:id>', views.details, name='details'),
    path('summary/', views.summary, name='summary'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('quotes/', views.quotes, name='quotes'),
]
