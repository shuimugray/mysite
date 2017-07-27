from django.http import HttpResponse
from django.shortcuts import  render
def mysite(request):
    return render(request,'about.html')