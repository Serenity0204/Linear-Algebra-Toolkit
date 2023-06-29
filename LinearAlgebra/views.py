from django.shortcuts import render


def index(request):
    if request.method == "POST":
        rows = int(request.POST.get("rows", 0))
        columns = int(request.POST.get("columns", 0))
        boxes = [
            ["box_{}_{}".format(i, j) for j in range(columns)] for i in range(rows)
        ]
        return render(request, "index.html", {"boxes": boxes})

    return render(request, "index.html")
