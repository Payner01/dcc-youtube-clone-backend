from django.urls import path
from comments import views

urlpatterns = [
    # path('comment/', views.CommentList.as_view()) 
    path('comment/', views.get_all_comments),
    path('', views.create_post),
]