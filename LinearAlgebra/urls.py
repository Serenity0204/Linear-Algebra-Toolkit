from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rref/", views.RREF_view, name="rref"),
]
