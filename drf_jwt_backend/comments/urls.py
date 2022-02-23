from django.urls import path
from comments import views

urlpatterns = [
    # path('comment/', views.CommentList.as_view()) 
    path('comments/', views.get_all_comments),
    path('', views.create_post),
]