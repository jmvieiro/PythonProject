from django.urls import path
from .views import *

urlpatterns = [
    path("", list_persons, name="list_persons"),
    path("create", create_person, name="create_person"),
    path("delete/<id>", delete_person, name="delete_person"),
]
