# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Car

# Create your views here.
def home(request):
    return render(request,"home.html",context= {"prueba":"Esta es una prueba"})

class carlist(ListView):
    template_name= 'cars/car_list.html'
    queryset = Car.objects.all()

class cardetail(DetailView):
    template_name= "cars/car_detail.html"
    queryset = Car.objects.all()

    def get_objet(self):
        return Car.objects.get(pk=1)
