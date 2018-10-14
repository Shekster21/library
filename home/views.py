from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

#model imports

from .models import userInfo

# Create your views here.

def index(request):
	return render(request,'homepage.html')

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			login(request,user)
			name = userInfo(user=user)
			return render(request,'profileview.html',{'name':name.user.first_name})
		else:
			return HttpResponse("account does not exist.")

	else:
		return HttpResponseRedirect(reverse('index'))