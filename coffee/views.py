from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

# Create your views here.
def home(request):
    coffee = Coffee.objects.all() #this just add is in step of adding html hoome
    return render(request,'home.html',{'coffee': coffee})
