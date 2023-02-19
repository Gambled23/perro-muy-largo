from django.shortcuts import render, HttpResponse

def login(request):
    #return render(request, 'login.html')
    return HttpResponse('login')

def home(request):
    #return render(request, 'home.html')
    return HttpResponse('home')

def generate_report(request):
    #return render(request, 'generate_report.html')
    return HttpResponse('generate_report')

def report_status(request):
    #return render(request, 'report_status.html')
    return HttpResponse('report_status')

def about_us(request):
    #return render(request, 'about_us.html')
    return HttpResponse('about_us')

def contact(request):
    #return render(request, 'contact.html')
    return HttpResponse('contact')

def faq(request):
    #return render(request, 'faq.html')
    return HttpResponse('faq')