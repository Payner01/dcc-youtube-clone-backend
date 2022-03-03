from django.urls import path
from comments import views

urlpatterns = [
    # path('comment/', views.CommentList.as_view()) 
    path('comments/<str:video_id>/', views.get_all_comments),
    path('', views.create_post),
    path('editcomments/<int:pk>/', views.update_comment),
    path('replies/<int:pk>/', views.get_replies),
    path('createreply/', views.create_reply)

]