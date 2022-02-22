from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .parsers import parse_string
from .forms import EntryForm, EntryModelForm
from .models import Entry

def all_entries(request):
    entries = Entry.objects.all()
    return render(request, 'entries/index.html', {'entries':entries})

def view_entry(request, entry_title):
    if not entry_exists(entry_title):
        url = reverse('create_entry', kwargs={})
        # TODO: add entry_title as default title
        return HttpResponseRedirect(url)

    entry = get_object_or_404(Entry, title__iexact=entry_title)
    context = {
        'entry_title': entry.title,
        'entry_text': parse_string(entry.wiki_entry)
    }
    return render(request, 'entries/view_entry.html', context)

def edit_entry(request, entry_title): 
    instance = get_object_or_404(Entry, title__iexact=entry_title)
    form = EntryModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance.title = form.cleaned_data['title']
        instance.wiki_entry = form.cleaned_data['wiki_entry']
        instance.save()

        # url = reverse('view_entry', kwargs={'entry_title': entry_title})
        url = reverse('view_entry', kwargs={'entry_title': form.cleaned_data['title'].lower()})
        return HttpResponseRedirect(url)
    return render(request, 'entries/edit_entry.html',  {'form': form})




def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            wiki_entry = form.cleaned_data['wiki_entry']

            # if (entry_exists(title)):
            #     # TODO: throw error
            #     return render(request, 'entries/create_entry.html', {'form': form})

            # TODO: try catch add
            new_entry = Entry(title=title, wiki_entry=wiki_entry)
            new_entry.save()
            # redirect to a new URL:
            url = reverse('view_entry', kwargs={'entry_title': title.lower()})
            return HttpResponseRedirect(url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()
        return render(request, 'entries/create_entry.html', {'form': form})


def create_entry_with_title(request, entry_title):
    context = {
        'wiki_text': 'Framework [Django] is written in [Python] programming language.'
    }
    return render(request, 'entries/index.html', context)



def entry_exists(entry_title):
    # TODO: refactor
    entry_count =  Entry.objects.filter(title__iexact=entry_title).count()
    print(entry_count)
    return entry_count > 0
