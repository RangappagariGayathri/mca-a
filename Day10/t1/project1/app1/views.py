from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')
def home2(request):
    return render(request,'home2.html')
