from rest_framework import serializers


from rest_framework import serializers
from codes.models import Post, Reply


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    loves_count = serializers.SerializerMethodField()
    user_has_loved = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ["loves", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_loves_count(self, instance):
        return instance.loves.count()

    def get_user_has_loved(self, instance):
        request = self.context.get("request")
        return instance.loves.filter(pk=request.user.pk).exists()


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    loves_count = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        exclude = ["updated_at", 'loves', 'post']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_loves_count(self, instance):
        return instance.loves.count()

    def get_post_id(self, instance):
        return instance.post.id
