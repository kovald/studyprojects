from django.http import HttpResponse
from django.shortcuts import render


from .models import Post
# Create your views here.


def post_create(request):
	return HttpResponse("<h1>Hello</h1>")

def post_detail(request): #retrieve
	context = {
	    "title": "Detail"
	}
	return render(request, "index.html", context)

def post_list(request): #list_items
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
    	"title": "List"
    }

    return render(request, "index.html", context)


#	if request.user.is_authenticated():
#		context = {
#	    	"title": "My User List"
#		}
#	else:
#		context = {
#	    	"title": "List"
#		}


def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse("<h1>Hello</h1>")