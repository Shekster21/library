from django.shortcuts import render
from django.http import HttpResponse
from requesthandler import useraddition
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	return HttpResponse('Hello World!')

@csrf_exempt
def useradd(request):
	word = useraddition(request)
	print(word)
	return HttpResponse()
