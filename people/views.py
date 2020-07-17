from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext
# from django.contrib.postgres.search import (SearchQuery,
#                                             SearchRank,
#                                             SearchVector)

from django_ajax.decorators import ajax

from .models import Person


class PersonListView(ListView):
    """Renders the home page with a Products List.
    If there is a GET request, performs a search."""
    model = Person
    context_object_name = 'people'


@ajax
def person_detail_ajax(request, person_id):
    active_person = Person.objects.get(pk=person_id)
    return render(request, 'people/person_detail.html', {'active_person': active_person})
