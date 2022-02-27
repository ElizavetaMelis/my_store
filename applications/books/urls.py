from django.urls import path

from applications.books.views import BookListView

urlpatterns = [
    path('book/', BookListView.as_view())
]