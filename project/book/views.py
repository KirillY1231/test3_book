from django.shortcuts import render, redirect

from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import *
from django.http import HttpResponseRedirect

from rest_framework import generics
# from .serializers import *

from django.views.generic import CreateView

import random

# Create your views here.

def index(request):
    context = {
        'persons': Person.objects.all(),
    }
    return render(request, 'book/index.html', context)

def search(request):
    search = request.POST.get('search')
    if search:
        persons = [person for person in Person.objects.all() if search.lower() in person.name.lower()+person.sname.lower()]

        context = {
            'persons': persons,
            'search': search,
        }
        return render(request, 'book/search.html', context)
    else:
        return redirect(reverse('book:index'))

def config(request):
    context = {
                'person_model_form': PersonModelForm(),
                # 'products': Product.objects.all(),
               }
    return render(request, 'book/config.html', context)

def new_person(request):
    new = PersonModelForm(request.POST, request.FILES)
    if new:
        saved = new.save(commit=False)
        if request.FILES != {}:
            new.photo = request.FILES['photo']

        new.save()
        return HttpResponseRedirect(reverse('book:index'))

def remove(request, pk):
    if pk:
        Person.objects.filter(pk=pk).delete()
        return HttpResponseRedirect(reverse('book:index'))

def edit(request, pk):

        person = Person.objects.get(pk=pk)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.sname = request.POST.get("sname")
            person.country = request.POST.get("country")
            person.city = request.POST.get("city")
            person.street = request.POST.get("street")
            person.url = request.POST.get("url")
            person.phone = request.POST.get("phone")

            if request.FILES != {}:
                person.photo = request.FILES['photo']


            person.save()
            return HttpResponseRedirect(reverse('book:index'))
        else:
            return render(request, "book/edit.html", {"person": person, 'person_model_form': PersonModelForm(initial={'name': person.name,
                                                                                                                      'sname': person.sname,
                                                                                                                      'country': person.country,
                                                                                                                      'city': person.city,
                                                                                                                      'street': person.street,
                                                                                                                      'url': person.url,
                                                                                                                      'phone': person.phone,
                                                                                                                      'photo': person.photo,})})


