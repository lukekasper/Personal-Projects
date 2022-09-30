import markdown2
import re

from django.shortcuts import render
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    if util.get_entry(title) is None:
        content = util.get_entry("Error")
    else:
        content = util.get_entry(title)

    return render(request, "encyclopedia/entry.html", {
        "content":  markdown2.markdown(content),
        "title": title
    })

def search(request):
    if request.method == "POST":
        entry = request.POST.get('q', 'not_found')
        if entry in util.list_entries():
            url = "encyclopedia:"+entry
            return HttpResponseRedirect(reverse(url))
        else:
            return render(request, "encyclopedia/search_results.html", {
                "results": search_results(entry)
            })
        search_results(entry)


def search_results(search):
    entries_list = util.list_entries()
    results = []
    for entry in entries_list:
        if re.search(search, entry) is not None:
            results.append(entry)
    return results




def markdown_converter(content):

    lines_list = content.split('\n')
    html_list = []

    for line in lines_list:

        # Headings
        head = re.match(r"^#*", line).end()
        if head > 0:
            line = re.sub(r"^#*", f"<h{head}>", line)
            line += f"</h{head}>"

        # List items
        if re.findall(r"\*", line) == ['*']:
            line = re.sub(r"\*", "<li>", line)
            line += "</li>"

        # Paragraph
        if re.match("^\w",line) is not None:
            line = "<p>" + line + "<\p>"

        html_list.append(line)

    # Unordered list brackets
    index = 0
    for line in html_list:

        if re.search(r"<li>", html_list[index]) is None and re.search(r"<li>", html_list[index + 1]) is not None:
            html_list[index] = "\n<ul>"
            index += 1
        elif re.search(r"<li>", html_list[index - 1]) is not None and re.search(r"<li>", html_list[index + 1]) is None:
            html_list[index + 1] = "</ul>\n"
            index += 1

        if index == len(html_list) - 1:
            if re.search(r"<li>", html_list[index]) is not None:
                html_list.append("</ul>")
            break

        index += 1

    content = '\n'.join(html_list)


