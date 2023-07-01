from django.shortcuts import render
import json


def index(request):
    return render(request, "index.html")


def RREF_view(request):
    if request.method == "POST":
        matrix_data = request.POST.get("matrixData", "[]")
        matrix = json.loads(matrix_data)

        context = {"matrix": matrix}
        return render(request, "rref.html", context)
