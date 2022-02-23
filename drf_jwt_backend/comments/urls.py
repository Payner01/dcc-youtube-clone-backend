from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()) 
]