from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    #return HttpResponse("Mon premer page web")
    return render(request, 'home.html')

def contact_view(request):
    #return HttpResponse("Mon page de contact")
    return render(request, 'contact.html')

def pagepri_view(request):
    return render(request, 'pagep.html')