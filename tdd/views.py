from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request,"tdd/dashboard.html")
def TDD(request):
    return render(request,"tdd/tdd.html")  

def Ahmadnagar(request):
    return render(request,"tdd/ahmadnagar.html")    

def Melghat(request):
    return render(request,"tdd/melghat.html")        