from django.urls import path, register_converter
from .views import CategoryCreate, NewsCreate, NewsList, NewsDetail, NewsFilters
from .converters import MyConverter

register_converter(MyConverter, 'filters')


urlpatterns = [
   path('category/create/', CategoryCreate.as_view()),
   path('create/', NewsCreate.as_view()),
   path('all/', NewsList.as_view()),
   path('detail/<int:pk>/', NewsDetail.as_view()),
   path('<filters:flt>/', NewsFilters.as_view()),
]
