from django.shortcuts import render
from school_gis.models import InstMsbvee12Apr2020
# Create your views here.
def SchoolDash(request):
    queryset = InstMsbvee12Apr2020.objects.all()
    return render(request,'school_gis/school_base.html',{'data':queryset})
