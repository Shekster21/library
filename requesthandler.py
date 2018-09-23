from django.http import HttpRequest
from home.forms import NewForm
def useraddition(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data
    return name


    