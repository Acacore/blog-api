import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    # Precise filtering
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    author = django_filters.CharFilter(field_name='author__username', lookup_expr='iexact')
    

    class Meta:
        model = Post
        # We define the fields above, so Meta can stay clean
        fields = ['category', 'author']