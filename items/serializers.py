from rest_framework import serializers
from .models import Item, Comment
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import StatusChoices

class GenericItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    status = serializers.ChoiceField(choices=StatusChoices.choices())
    created_at = serializers.DateTimeField(read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    days_since_created = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    def get_days_since_created(self, obj):
        return obj.days_since_created

    def get_comment_count(self, obj):
        return obj.comment_count

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class GenericCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    text = serializers.CharField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    user_items = serializers.SerializerMethodField()
    is_own_profile = serializers.SerializerMethodField()

    def get_user_items(self, obj):
        from .serializers import ItemSerializer
        return ItemSerializer(Item.objects.filter(user=obj).order_by('-created_at'), many=True).data

    def get_is_own_profile(self, obj):
        request = self.context.get('request')
        return request and request.user.is_authenticated and request.user.id == obj.id

class NestedCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'user']

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = NestedCommentSerializer(many=True, read_only=True)
    days_since_created = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    def get_days_since_created(self, obj):
        return obj.days_since_created

    def get_comment_count(self, obj):
        return obj.comment_count

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'item', 'user', 'text', 'created_at']

    def validate_text(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Comment is too short.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
