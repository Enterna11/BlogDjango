from django.contrib.auth import get_user_model
from .models import Categories

User = get_user_model()


class MyConverter:
    regex = '[a-z]+[=][^/]+'

    @staticmethod
    def to_python(value):
        value = value.split('=')
        if value[0] == 'category':
            value[1] = Categories.objects.get(title=value[1]).id
        elif value[0] == 'author':
            value[1] = User.objects.get(username=value[1]).id
        return value

    @staticmethod
    def to_urls(value):
        return value
