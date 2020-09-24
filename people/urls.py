from django.urls import path
from .views import PersonListView, person_detail_ajax

urlpatterns = [
    path('', PersonListView.as_view(), name="person-list"),
    path('person/ajax/<int:person_id>/', person_detail_ajax,
         name="person-detail-ajax"),
]
