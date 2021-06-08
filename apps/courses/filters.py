import django_filters
from django.db.models import Q

from apps.courses.models import Course


class CourseFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(label='所属app', method='name_filter', help_text='所属app')

    def name_filter(self, queryset, name, value):
        return queryset.filter(name=value)

    class Meta:
        model = Course
        fields = ['name']
