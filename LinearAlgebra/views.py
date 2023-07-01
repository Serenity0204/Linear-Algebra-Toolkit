from django.shortcuts import render, redirect
import json
from .utils import find_rref


def index(request):
    return render(request, "index.html")


def rref_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        original_matrix = json.loads(matrix_data)
        if not original_matrix:
            return redirect("index")

        matrix = find_rref(original_matrix)
        operation = "RREF"
        context = {
            "matrix": matrix,
            "original_matrix": original_matrix,
            "operation": operation,
        }
        return render(request, "matrix.html", context)
    else:
        return redirect("index")


## need to restructure later
def nullspace_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        original_matrix = json.loads(matrix_data)
        if not original_matrix:
            return redirect("index")

        matrix = find_rref(original_matrix)
        operation = "Nullspace"
        context = {
            "matrix": matrix,
            "original_matrix": original_matrix,
            "operation": operation,
        }
        return render(request, "matrix.html", context)
    else:
        return redirect("index")
