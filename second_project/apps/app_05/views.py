from django.shortcuts import render, HttpResponse, redirect

# app_05
def edit(request, number):
    return HttpResponse("placeholder to edit blog " + number)