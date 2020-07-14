from django.urls import path
from .views import PersonListView

urlpatterns = [
    path('', PersonListView.as_view(), name="person-list")
]
