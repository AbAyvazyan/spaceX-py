from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'title', 'subtitle']

    def validate(self, data):
        if not self.instance:
            if Post.objects.count() >= 4:
                raise serializers.ValidationError("Maximum number of items (4) reached.")
        return data