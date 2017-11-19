# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    comment= models.TextField()
    author = models.ForeignKey('auth.User')

def __str__(self):
    return self.name
