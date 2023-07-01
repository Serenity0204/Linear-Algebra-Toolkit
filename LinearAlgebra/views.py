from django.shortcuts import render, redirect
import json
from .utils import *


def index(request):
    return render(request, "index.html")


def rref_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        original_matrix = json.loads(matrix_data)
        if not original_matrix:
            return redirect("index")

        matrix = find_rref(original_matrix)
        context = {"matrix": matrix, "original_matrix": original_matrix}
        return render(request, "rref.html", context)
    else:
        return redirect("index")


## need to restructure later
def nullspace_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        original_matrix = json.loads(matrix_data)
        if not original_matrix:
            return redirect("index")

        nullspace = find_nullspace(original_matrix)
        context = {"spaces": [nullspace], "original_matrix": original_matrix}
        return render(request, "space.html", context)
    else:
        return redirect("index")


def colspace_and_rowspace_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        original_matrix = json.loads(matrix_data)
        if not original_matrix:
            return redirect("index")
        colspace = find_colspace(original_matrix)
        rowspace = find_rowspace(original_matrix)
        context = {"spaces": [colspace, rowspace], "original_matrix": original_matrix}
        return render(request, "space.html", context)
    else:
        return redirect("index")
