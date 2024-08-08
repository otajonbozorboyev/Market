from django.shortcuts import render
from .models import Contact

def contactView(request):
    contact = Contact.objects.all().first()
    return render(request, 'contact.html',
                  {'contact': contact})