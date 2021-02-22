# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tb_stock_daily(models.Model) :
	stock_name = models.CharField(max_length=20, blank=True) #null=True
	openp = models.FloatField(blank=True)
	high = models.FloatField(blank=True)
	low = models.FloatField(blank=True)
	close = models.FloatField(blank=True)
	volume = models.IntegerField(blank=True)
	market_date = models.DateField(auto_now=False, auto_now_add=False,blank=True)
	
	def __str__(self):
		return "%s"%(format(self.stock_name))