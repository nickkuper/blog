#coding: utf-8
from django.db import models
#from django.contrib.sites.models import Site


class Post(models.Model):
    title = models.CharField(max_length=225)
    datettime = models.DateTimeField(u'Дата публикации')
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
