# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.contrib.auth.models import User
from .models import Tb_stock_daily

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def show_data(request) :
	if request.method == 'POST' :
		stock_nm = request.POST.get('stock_name')
		date_from = request.POST.get('date_from')
		date_to = request.POST.get('date_to')


		item = Tb_stock_daily.objects.filter(stock_name = stock_nm,
											market_date__range = [date_from, date_to])

	else :
		item = Tb_stock_daily.objects.filter(stock_name = 'IHSG')

	context = {
		'item' 	:	item,
	}
	#return render(request, 'listuser.html', context)
	return render(request, 'databei/list_data.html', context)
