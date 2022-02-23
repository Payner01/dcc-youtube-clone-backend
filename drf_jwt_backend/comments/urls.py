from django.urls import path
from comments import views

urlpatterns = [
    # path('comment/', views.CommentList.as_view()) 
    path('comments/', views.get_all_comments),
    path('', views.create_post),
    path('editcomments/<int:pk>/', views.update_comment),
    path('commentsreplies/<int:pk>/', views.get_comment_replies)
]