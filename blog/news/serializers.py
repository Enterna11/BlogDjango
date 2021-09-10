from rest_framework import serializers
from .models import News, Categories


class CategoryCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):

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
        fields = ('id', 'title', 'author', 'category')
