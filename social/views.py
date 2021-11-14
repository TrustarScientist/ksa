from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def usn(request, username="not found"):
    return HttpResponse("<h1>profile page for "+username+"</h1>")