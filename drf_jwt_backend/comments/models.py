from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=250) 