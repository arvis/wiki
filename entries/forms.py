from django import forms
from django.forms import ModelForm
from .models import Entry

class EntryForm(forms.Form):
    title = forms.CharField(label='Wiki title *',required=True, max_length=200)
    wiki_entry = forms.CharField(label='Wiki entry *',widget=forms.Textarea(attrs={"rows":5, "cols":50}), required=True, max_length=200)


class EntryModelForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'wiki_entry']    