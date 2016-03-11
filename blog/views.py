from django.shortcuts import render
from blog.models import Entry,Slider,Portofolio
from django.http import HttpResponse
from django.template import Context, loader
# from markdown import MarkdownFormField


from django.contrib.auth.models import User
# from .fields import MarkdownFormField
# from .widgets import MarkdownWidget
# Create your views here.

def home(request):
	entry_all = Entry.objects.all()
	c =Context({'entry_all' : entry_all,})
	template = "home.html"
	return render (request, template, c)


def tutorial(request):
	
	porto_all = Portofolio.objects.all()
	c =Context({'porto_all' : porto_all,				
		})

	template = "blog-single.html"
	return render (request, template, c)



def index(request):
	# user = User.objects.get(username=username)
	entry_all = Entry.objects.all().order_by("-timestamp")
	slider_all = Slider.objects.all()
	c =Context({'entry_all' : entry_all,
				'slider_all' :slider_all,
				# 'username' : username,
		})

	template = "index.html"
	return render (request, template, c)


# Sortir data pokok Entry
# +++++++++++++++++++++++++++++++++++++++++++++++++++
def tester(request):

	entry_all = Entry.objects.all()
	slider_all = Slider.objects.all().filter(title ='Arduino')
	c =Context({'entry_all' : entry_all,
				'slider_all' :slider_all,
				# 'username' : username,
		})

	template = "tester.html"

	return render (request, template, c)





# ==========================================================================
# this is menu page 

def blender(request):
	entry_all = Entry.objects.all().filter(title ='blender')
	container = ({'entry_all' : entry_all,

		})
	template = "bloging/blog_output.html"
	return render(request,template,container)


