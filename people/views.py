from django.views.generic import ListView
# from django.contrib.postgres.search import (SearchQuery,
#                                             SearchRank,
#                                             SearchVector)

from .models import Person


class PersonListView(ListView):
    """Renders the home page with a Products List.
    If there is a GET request, performs a search."""
    model = Person
    context_object_name = 'people'
