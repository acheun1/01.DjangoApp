from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# def index(req):
#     return render(req,'app_01/index.html')
# app_01
def index(request):
    return HttpResponse("placeholder to display all the list of blogs")
