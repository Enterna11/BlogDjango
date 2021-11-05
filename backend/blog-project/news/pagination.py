from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from math import ceil


class AllNewsPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 100

    def num_pages(self):
        return ceil(self.page.paginator.count / self.page_size)

    def next_page_number(self):
        number = self.page.number + 1
        if number > self.num_pages():
            return None
        return number

    def previous_page_number(self):
        number = self.page.number - 1
        if number < 1:
            return None
        return number

    def get_paginated_response(self, data):
        return Response({
            'chapter': 'all',
            'link': {
                'next':  self.next_page_number(),
                'previous': self.previous_page_number(),
                'current': self.page.number
            },
            'size': self.page.paginator.count,
            'results': data,
            })


class CategoryPagination(AllNewsPagination):
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'chapter': 'category',
            'link': {
                'next': self.next_page_number(),
                'previous': self.previous_page_number(),
                'current': self.page.number
            },
            'size': self.page.paginator.count,
            'results': data
        })


class SearchPagination(AllNewsPagination):
    page_size = 5
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'chapter': 'search',
            'link': {
                'next': self.next_page_number(),
                'previous': self.previous_page_number(),
                'current': self.page.number
            },
            'size': self.page.paginator.count,
            'results': data
        })
