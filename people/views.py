import random

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db import connection
from django.contrib.postgres.search import (SearchQuery,
                                            SearchRank,
                                            SearchVector)

from django_ajax.decorators import ajax

from .models import Person


class PersonListView(ListView):
    """Renders the home page with a Products List.
    If there is a GET request, performs a search."""
    model = Person
    seed = ''

    def get_queryset(self):
        """Returns either all Products or a query appropriately."""
        if 'query' in self.request.GET:
            # Returns all people if there's no query
            if (self.request.GET['query'] == ''):
                self.postgres_setseed()
                return super(ListView, self).get_queryset().order_by('?')
            else:
                # Performs a full text search using Postgres database
                # functionality, weighting tags above other text.
                self.user_query = self.request.GET['query']
                self.vector = SearchVector(
                    'name',
                    'blurb',
                    'story',
                    weight='B') + SearchVector(
                        'tags', weight='A')
                self.query = SearchQuery(self.user_query)
                self.rank = SearchRank(self.vector, self.query)

                # Returns search results in order of rank,
                # removing items with no rank.
                return Person.objects.annotate(
                    rank=self.rank).order_by(
                    '-rank').filter(rank__gt=0)
        else:
            self.postgres_setseed()
            return super(ListView, self).get_queryset().order_by('?')

    def get(self, *args, **kwargs):
        page = self.request.GET.get('page')
        if not page or page == '1':
            self.generate_seed()

        self.seed = self.get_seed()

        return super(ListView, self).get(*args, **kwargs)

    def get_seed(self):
        if not self.request.session.get('seed'):
            return self.generate_seed()
        else:
            return self.request.session.get('seed')

    def generate_seed(self):
        # self.request.session['seed'] = random()
        self.request.session['seed'] = random.random()
        return self.request.session['seed']

    def postgres_setseed(self):
        cursor = connection.cursor()
        cursor.execute("SELECT setseed(%s);" % (self.seed,))
        cursor.close()

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)

        # Paginates people for the infinite scroll feature.
        people = context['object_list']
        paginator = Paginator(people, 3)
        page_number = self.request.GET.get('page')

        # Pagination is more complicated with a query
        # so this is necessary for the people to display properly and
        # not repeat the first page infinitely.
        if 'query' in self.request.GET:
            if 'page' in self.request.GET['query']:
                page_number = self.request.GET['query'].rpartition('=')[-1]
            keyword = self.request.GET['query'].split('?')[0]
            context['keyword'] = keyword

        page_obj = paginator.get_page(page_number)
        context['people'] = page_obj
        return context


class PersonDetailView(DetailView):
    """Renders a separate page specifically for each Person object"""
    model = Person
    context_object_name = 'active_person'


@ajax
def person_detail_ajax(request, person_id):
    active_person = Person.objects.get(pk=person_id)
    video = active_person.video

    return render(request, 'people/includes/detail_modal.html',
                  {'active_person': active_person}), {'video': video}
