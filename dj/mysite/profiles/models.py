# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	name=models.CharField(max_length=120)
	description=models.TextField(default='description')
	location=models.CharField(max_length=120,default='mulocation',blank=True,null=True)
	job=models.CharField(max_length=120,null=True)

	def __unicode__(self):
			return self.name
 