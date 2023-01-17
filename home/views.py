from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"this is sent",
        "variable2":"this is sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("This is Homepage!")
    #return render(request, 'index.html')

def about(request):
    #return HttpResponse("This is Aboutpage!")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("This is servicespage!")
    return render(request, 'services.html')

def contact(request):
    #return HttpResponse("This is contactpage!")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        contact= Contact(name=name, email=email, phone=phone,password=password)
        ##,date=datetime.today()
        contact.save()
        messages.success(request, 'Form submitted successfully!!!')
    return render(request, 'contact.html')# cant keep context cos we have send no variables in here