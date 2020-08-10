from django.shortcuts import render
from templates import *
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from .models import * 

def contact(request):
    schedule = Schedule.objects.all()
    address = StudioAddress.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("#")
    else:
        template_name = "contact.html"
        return render(request, template_name, {'schedule' : schedule, 'address' : address } ) 

def blog(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("#")
    else:
        template_name = "blog.html"
        return render(request, template_name, {} )
    

def classes(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect("#")
    else:
        template_name = "classes.html"
        return render(request, template_name, {} )
    

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("#")
    else:
        template_name = "index.html"
        return render(request, template_name, {} )   




def aboutus(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("#")
    else:
        template_name = "about-us.html"
        return render(request, template_name, {} )
      

def shop(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("#")
    else:
        template_name = "elements.html"
        return render(request, template_name, {} )
      


