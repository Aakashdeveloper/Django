from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    #3return HttpResponse('<h1>Hii To Edureka</h1>')
    return render(request,'eduapp/display.html')
