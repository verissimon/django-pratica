from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    if req.method == "GET":
        return render(req, 'index.html')