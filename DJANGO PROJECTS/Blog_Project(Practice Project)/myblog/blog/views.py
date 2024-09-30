from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

