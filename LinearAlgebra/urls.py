from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rref/", views.rref_view, name="rref"),
    path("nullspace/", views.nullspace_view, name="nullspace"),
    path(
        "colpace-and-rowspace/",
        views.colspace_and_rowspace_view,
        name="colspace_and_rowspace",
    ),
]
