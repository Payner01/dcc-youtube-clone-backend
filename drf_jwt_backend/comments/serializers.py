from rest_framework import serializers
from .models import Reply, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    # code below gets all information about comment plus the reply.
    # comment = CommentSerializer(many=False, read_only=True)
    class Meta:
        model = Reply
        fields = '__all__' 