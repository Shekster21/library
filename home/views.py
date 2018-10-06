from django.shortcuts import render
from django.http import HttpResponse
#from requesthandler import useraddition
from django.views.decorators.csrf import csrf_exempt

from .forms import NewForm
# Create your views here.

def index(request):
	return render(request,'homepage.html')

@csrf_exempt
def useradd(request):
	if request.method == "POST":
		form = NewForm(request.POST)
		if form.is_valid():
			print("hello")
	return HttpResponse()