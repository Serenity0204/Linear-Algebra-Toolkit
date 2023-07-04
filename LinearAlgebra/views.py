from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import MatrixStore
from .utils import *
import json


def index(request):
    try:
        matrix = MatrixStore.objects.latest("id")
        context = {"global_matrix": matrix}
    except ObjectDoesNotExist:
        context = {"global_matrix": None}
    return render(request, "index.html", context)


def generate_matrix_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        original_matrix = json.loads(matrix_data)
        if not original_matrix:
            return redirect("index")

        # Save the matrix in the database
        matrix = MatrixStore(data=original_matrix)
        matrix.save()

    return redirect("index")


def rref_view(request):
    if request.method == "POST":
        try:
            matrix = MatrixStore.objects.latest("id")
        except ObjectDoesNotExist:
            return redirect("index")

        original_matrix = matrix.data
        rref_matrix = find_rref(original_matrix)
        context = {"matrix": rref_matrix, "original_matrix": original_matrix}
        return render(request, "rref.html", context)
    else:
        return redirect("index")


def nullspace_view(request):
    if request.method == "POST":
        try:
            matrix = MatrixStore.objects.latest("id")
        except ObjectDoesNotExist:
            return redirect("index")

        original_matrix = matrix.data
        nullspace = find_nullspace(original_matrix)
        context = {"spaces": [nullspace], "original_matrix": original_matrix}
        return render(request, "space.html", context)
    else:
        return redirect("index")


def colspace_and_rowspace_view(request):
    if request.method == "POST":
        try:
            matrix = MatrixStore.objects.latest("id")
        except ObjectDoesNotExist:
            return redirect("index")

        original_matrix = matrix.data
        colspace = find_colspace(original_matrix)
        rowspace = find_rowspace(original_matrix)
        context = {"spaces": [colspace, rowspace], "original_matrix": original_matrix}
        return render(request, "space.html", context)
    else:
        return redirect("index")
