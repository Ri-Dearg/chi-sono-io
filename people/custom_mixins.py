import random
from django.db import connection


class RandomQuerysetMixin(object):
    """
        Filter/Sort by "random" without breaking pagination.
        Requirements:
            Postgres
            Django Sessions

        Todo:
            - Support for MySQL (replace setseed, w/ order by random(seed))
            - Support for larger datasets (get rid of '?')
    """
    randomize = True
    page_param = 'page'  # page slug to determine first page
    paginate_by = 3    # will be used to properly handle larger datasets
    large_dataset = False   # will be used to properly handle larger datasets

    seed = ''

    def get_queryset(self):
        if self.randomize:
            self.postgres_setseed()
            qs = super(RandomQuerysetMixin, self).get_queryset().order_by('?')
        else:
            qs = super(RandomQuerysetMixin, self).get_queryset()

        return qs

    def get(self, *args, **kwargs):
        page = self.request.GET.get(self.page_param)
        if not page or page == '1':
            self.generate_seed()

        self.seed = self.get_seed()

        return super(RandomQuerysetMixin, self).get(*args, **kwargs)

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