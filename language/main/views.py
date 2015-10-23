from django.shortcuts import render
import datetime

# Create your views here.
def main(request):
    context = {'message':'Django 很棒','now': datetime.datetime.now()} 
    return render(request, 'main/main.html', context)