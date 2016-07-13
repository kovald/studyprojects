from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def post_home(request):
	return HttpResponse("<h1>Hello</h1>")

def post_detail(request): #retrieve
	return HttpResponse("<h1>Hello</h1>")

def post_list(request): #list_items
	return HttpResponse("<h1>Hello</h1>")

def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse("<h1>Hello</h1>")