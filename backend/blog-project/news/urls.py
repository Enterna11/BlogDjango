from django.urls import path, register_converter
from .views import CategoryCreate, NewsCreate, NewsList, NewsDetail, NewsFilters, CategoriesList, CategoryNews, \
                   SearchNews, CommentCreate
from .converters import MyConverter

register_converter(MyConverter, 'filters')


urlpatterns = [
   path('category/all/', CategoriesList.as_view()),
   path('category/create/', CategoryCreate.as_view()),
   path('category/<str:category_name>/', CategoryNews.as_view()),
   path('create/', NewsCreate.as_view()),
   path('all/', NewsList.as_view()),
   path('<int:pk>/', NewsDetail.as_view()),
   path('<filters:flt>/', NewsFilters.as_view()),
   path('search/<str:params>', SearchNews.as_view()),
   path('comment/create', CommentCreate.as_view())
]
