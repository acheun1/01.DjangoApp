from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# def index(req):
#     return render(req,'app_01/index.html')
# app_04
def show(request, number):
    print(str(number))
    return HttpResponse("placeholder to display blog " + number)