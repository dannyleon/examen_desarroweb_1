# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Car
from .forms import CarModelForm
from .mixin import FormUserNeededMixin

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

class CarListView(ListView):
    template_name = 'cars/list.html'
    #queryset= Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs= Car.objects.all()
        print self.request.GET
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(


                            Q(make__icontains= query) |
                            Q(Type__icontains= query)|
                            Q(year__icontains= query)|
                            Q(colour__icontains= query)|
                            Q(price__icontains= query)


                            #Q(user__username__icontains= query)

                          )

        return qs


    def get_context_data(self, *args, **kwargs):
        context = super(CarListView, self).get_context_data(*args,**kwargs)
        print context
        context['create_form'] = CarModelForm()
        context['create_url'] = reverse_lazy("CarCreate")
        return context

    def upload_file(request):
        if request.method == 'POST':
            form = CarModelForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                form.save()
                return HttpResponseRedirect('/cars/listc')
        else:
            form = CarModelForm()
            return render(request, 'list.html', context)

class CarCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    form_class = CarModelForm
    template_name ="cars/list.html"
    success_url = "/cars/listc"
    login_url= "/admin"

class CarUpdateView (UpdateView):
    queryset = Car.objects.all()
    form_class = CarModelForm
    template_name = "cars/update_view.html"
    success_url = "/cars/listc"

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model= Car
    template_name = "cars/delete_confirm.html"
    success_url = reverse_lazy("car_list")
