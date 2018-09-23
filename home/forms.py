from django import forms
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class NewForm(forms.Form):
    name = forms.CharField()