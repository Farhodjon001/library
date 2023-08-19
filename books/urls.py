from django.urls import path
from .views import BookLisApiView,BookDetailApiView,BookUpdateApiView,BookDeleteApiView,BookCreateApiView

urlpatterns=[
    path("books/",BookLisApiView.as_view()),
    path("books/<int:pk>/update/",BookUpdateApiView.as_view()),
    path("books/<int:pk>/delete/",BookDeleteApiView.as_view()),
    path("books/<int:pk>/",BookDetailApiView.as_view()),
    path("books/create/",BookCreateApiView.as_view()),
    # path("books/",book_list_view)

]
