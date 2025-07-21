from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Optional: send email or save to database
        return HttpResponse("Thanks for contacting us!")
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')