from django.shortcuts import render, HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World! This is app one.')

# def login(request):
#     return HttpResponse('You are logged in from first app')

def index(request):
    return render(request, 'AppOne/index.html')

def login(request):
    return render(request, 'AppOne/login.html')