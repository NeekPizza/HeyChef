from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request,'pgp/index.html')

def recipes(request):
    return render(request,'pgp/recipes.html')

def details(request, uri):
    context = {
        'uri' : uri
    }
    print uri
    return render(request,'pgp/details.html',context)
