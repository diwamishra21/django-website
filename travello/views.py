from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Destination, Contact
from .forms import ContactForm

# Create your views here.

def index(request):

    dests = Destination.objects.all()
    return render(request,'travello/index.html',{'dests': dests})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Thanks for contacting us! We will get back to you soon')
            return redirect('/')
        else:
            messages.info(request,'Some error in saving form!')
            return redirect('/')
    else:
        form = ContactForm()
        return render(request,'travello/contact.html', {'form': form})


def contact_list(request):
    contact = Contact.objects.all()
    return render(request,'travello/contact_list.html',{'contact': contact})


def contact_edit(request, id):  
    contact = Contact.objects.get(id=id)  
    return render(request,'travello/contact_edit.html', {'contact':contact})  


def contact_update(request, id):  
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/contact_list")  
    return render(request, 'travello/contact_edit.html', {'contact': contact})  

    
def contact_destroy(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/contact_list") 