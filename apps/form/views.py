# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import string
import random

def index(request):
	try:
		if request.session['count'] != None:
			return render(request, "form/index.html")
		else:
			request.session['count'] = 0
			return render(request, "form/index.html")
	except:
		request.session['count'] = 0
		return render(request, "form/index.html")


def process(request):
	print request.method
	if request.method=="POST":
		request.session['name']=request.POST['name']
		request.session['location']=request.POST['location']
		request.session['language']=request.POST['language']
		request.session['comment']=request.POST['comment']
		print '*'*50
		print request.POST
		print '*'*50
		request.session['count'] += 1
		return redirect('/result')
	else:
		return redirect('/')
def result(request):
	return render(request, "form/result.html")

