from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_display(request, title):
    if title not in views.list_entries():
        return render(request, "entries/error.html")
    else:
        return render(request, f"encyclopedia/{title}.html")
        content = util.get_entry(title)