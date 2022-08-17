from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest

def main(request: HttpRequest):
    return render(request, 'main.html')
