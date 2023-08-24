from django.shortcuts import render,redirect
from .models import Appointment, Service, Complain
from .utils import random_string_generator
from django.contrib import messages
import random
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def book(request):
    services_ = Service.objects.values_list('name',flat=True)
    services = []
    for i in services_:
        services.append(i)
    context = {
        'services':services,
    }
    return render(request,'book.html',context=context)

def home(request):
    services = Service.objects.all()

    return render(request,'home.html',{'services':services})

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        obj = Complain.objects.create(name=name,email=email,subject=subject,message=message)
        messages.info(request,"Thanks for reaching out.We will get in touch soon!!!")
        return redirect('booking/contact')
    return render(request,'contact.html')


def services(request):
    return render(request,'service.html')

def appointment(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')

        obj = Appointment.objects.create(name=name,email=email,service=service,contact=contact,date=date,time=time,note=note)
        appointment.save

        return redirect('home')
    return redirect('home')


def success(request):
    print(request.POST)
    order_id = random_string_generator()
    email = request.POST.get('email')
    service = request.POST.get('service')
    date = request.POST.get('date')
    time = request.POST.get('time')
    name  = request.POST.get('name')
    obj = Service.objects.filter(name=service).first()
    try:
        amount = obj.price
    except:
        amount = "N/A"
    context = {
        'email':email,
        'name':name,
        'service':service,
        'date':date,
        'time':time,
        'order_id':order_id,
        'contact':contact,
        'amount':amount,
    }
    return render(request,'success.html',context=context)