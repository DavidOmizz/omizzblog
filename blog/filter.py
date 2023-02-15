import django_filters
from .models import Post

class FilterForm (django_filters.FilterSet):
    
    class Meta:
        model = Post
        fields = {'title':['exact']}

