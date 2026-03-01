import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    # Lookup by title, category, authoor and content with case-insensitive partial matching
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')
    author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='exact')
    # Filter by date range (e.g., 'created_at__gte' for "after this date")
    published_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Post
        fields = ['title', 'category', 'author', 'published_after']