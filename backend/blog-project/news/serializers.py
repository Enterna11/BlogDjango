from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import News, Categories, Comment


class CategoryListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class CategoryCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(slug_field='title', queryset=Categories.objects.all())

    class Meta:
        model = News
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', queryset=Categories.objects.all())

    class Meta:
        model = News
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    news = serializers.SlugRelatedField(slug_field='title', queryset=News.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(slug_field='title', queryset=Categories.objects.all())
    news_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'
