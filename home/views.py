from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact

def home(request):
    context = {'name':'Manu', 'job':'Developer' }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        # print("This is POST")
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name,email,message)
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        print("Data uploaded")
    return render(request, 'contact.html')