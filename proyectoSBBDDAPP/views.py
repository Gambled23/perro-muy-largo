from django.shortcuts import render, HttpResponse

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def generate_report(request):
    return render(request, 'generate_report.html')

def report_status(request):
    return render(request, 'report_status.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')