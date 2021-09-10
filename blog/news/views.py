from rest_framework import generics
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategoryCreateSerializers, NewsDetailSerializer, NewsListSerializer
from .models import News
from .permissions import Owner


class CategoryCreate(generics.CreateAPIView):

    """Создание категорий"""

    serializer_class = CategoryCreateSerializers


class NewsCreate(generics.CreateAPIView):

    """Создание статьи"""

    serializer_class = NewsDetailSerializer


class NewsList(generics.ListAPIView):

    """Показываем всем статьи"""

    serializer_class = NewsListSerializer
    queryset = News.objects.all()


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):

    """Показываем отдельную статью"""

    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()
    permission_classes = (Owner,)


class NewsFilters(APIView):

    """Вывод записей с указанными фильтрами"""

    def get(self, request, flt: dict):
        news = get_list_or_404(News.objects.filter(flt))
        serializer = NewsListSerializer(news, many=True)
        return Response({'news': serializer.data})
