from dataclasses import field
from rest_framework import serializers
from .models import Reply, Comment
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only = True)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only = True)
    class Meta:
        model = Reply
        fields = '__all__' 