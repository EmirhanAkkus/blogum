from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def anasayfaView(request):
    return HttpResponse('Merhaba Dünya. ')

class AnasayfaView(TemplateView):
    template_name= 'home.html'