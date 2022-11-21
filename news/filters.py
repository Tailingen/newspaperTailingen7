from django_filters.widgets import DateRangeWidget
from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
   time_in = DateFromToRangeFilter(widget = DateRangeWidget(attrs={'placeholder': 'ГГГГ-ММ-ДД'}))
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'author': ['exact'],
       }
#       filter_overrides = {
#           models.DateField: {
#               'filter_class': RangeFilter,
#               'extra': lambda f: {'widget': RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}),},
#           }
#       }