from django.shortcuts import render

# Create your views here.
def fgis_map(request):
    return render(request,'fgis_map/map.html')