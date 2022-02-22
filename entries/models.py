from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200,unique=True,blank=False)
    wiki_entry = models.TextField(blank=False, null=False)
    views = models.IntegerField(default=0)