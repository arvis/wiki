from django.shortcuts import render
from django.http import HttpResponse
from .parsers import parse_string
from django.urls import reverse

def all_entries(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    parsed = parse_string('aaaaa [bbbb] cccc')
    context = {
        'wiki_text': 'Framework [Django] is written in [Python] programming language.'
    }
    return render(request, 'entries/index.html', context)

def view_entry(request, entry_title):
    context = {
        'entry_title': entry_title,
        'entry_text': 'Framework [Django] is written in [Python] programming language.'
    }
    return render(request, 'entries/view_entry.html', context)

def edit_entry(request, entry_title):
    context = {
        'wiki_text': 'Framework [Django] is written in [Python] programming language.'
    }
    return render(request, 'entries/index.html', context)

def create_entry(request):
    context = {
        'wiki_text': 'Framework [Django] is written in [Python] programming language.'
    }
    return render(request, 'entries/index.html', context)


def create_entry_with_title(request, entry_title):
    context = {
        'wiki_text': 'Framework [Django] is written in [Python] programming language.'
    }
    return render(request, 'entries/index.html', context)


