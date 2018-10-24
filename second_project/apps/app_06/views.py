from django.shortcuts import render, HttpResponse, redirect

# app_06
# def delete(request):
#     return redirect('/')
def delete(request, number):
    return HttpResponse("placeholder to delete blog " + number)