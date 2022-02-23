from rest_framework import serializers
from .models import Reply, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    user = CommentSerializer(many=False, read_only=True)
    class Meta:
        model = Reply
        fields = '__all__' 