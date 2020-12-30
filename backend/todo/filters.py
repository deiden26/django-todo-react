import django_filters

from .models import Todo

class TodoFilterset(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    title_exact = django_filters.CharFilter(field_name='title')
    description = django_filters.CharFilter(lookup_expr='icontains')
    completed = django_filters.BooleanFilter()
    tag = django_filters.CharFilter(field_name='tags__name')
    min_tag_count = django_filters.NumberFilter(
        field_name='tags__count', lookup_expr='gt')

    class Meta:
        model = Todo
        fields = (
            'title',
            'title_exact',
            'description',
            'completed',
            'tag',
            'min_tag_count',
        )
