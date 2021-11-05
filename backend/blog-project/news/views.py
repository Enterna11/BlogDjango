from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .serializers import CategoryCreateSerializers, NewsDetailSerializer, NewsListSerializer, CategoryListSerializers, \
                         CommentCreateSerializer, NewsCreateSerializer
from .models import News, Categories, Comment
from .permissions import Owner
from django.db.models import Q
from .pagination import AllNewsPagination, CategoryPagination, SearchPagination


class CategoryNews(generics.ListAPIView):

    serializer_class = NewsListSerializer
    model = News
    pagination_class = CategoryPagination

    def get_queryset(self):
        data = self.kwargs['category_name']
        queryset = self.model.objects.filter(category__title=data)
        return queryset


class CategoriesList(generics.ListAPIView):

    """Показ категорий"""

    serializer_class = CategoryListSerializers
    queryset = Categories.objects.all()


class CategoryCreate(generics.CreateAPIView):

    """Создание категорий"""

    serializer_class = CategoryCreateSerializers
    permission_classes = (IsAdminUser,)


class NewsCreate(generics.CreateAPIView):

    """Создание статьи"""

    serializer_class = NewsCreateSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class NewsList(generics.ListAPIView):

    """Показываем все статьи"""

    serializer_class = NewsListSerializer
    queryset = News.objects.filter(is_published=True)
    pagination_class = AllNewsPagination


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):

    """Показываем отдельную статью"""

    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()
    permission_classes = (Owner,)


class NewsFilters(generics.ListAPIView):

    """Вывод записей с указанными фильтрами"""

    serializer_class = NewsListSerializer
    model = News
    pagination_class = AllNewsPagination

    def get_queryset(self):
        data = self.kwargs['flt']
        queryset = self.model.objects.filter(data)

        return queryset


class SearchNews(generics.ListAPIView):

    """Поиск"""

    serializer_class = NewsListSerializer
    model = News
    pagination_class = SearchPagination

    def get_queryset(self):
        params = self.kwargs['params'].split()
        if len(params) > 1:
            queryset = self.model.objects.filter(
                (Q(author__username__icontains=params[0]) & Q(title__contains=params[1].capitalize())) |
                (Q(author__username__icontains=params[1]) & Q(title__contains=params[0].capitalize()))
            )
        else:
            queryset = self.model.objects.filter(
                Q(author__username__icontains=params[0]) | Q(title__contains=params[0].capitalize())
            )

        return queryset


class CommentCreate(generics.CreateAPIView):

    """Создание комментария"""

    serializer_class = CommentCreateSerializer
    model = Comment
    permission_classes = (IsAuthenticated,)
