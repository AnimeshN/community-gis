from django.shortcuts import render
from django.conf import settings
# Create your views here.
def fgis_map(request):
    context = {'site_url':settings.MY_SITE_URL}
    return render(request,'fgis_map/map.html',context)