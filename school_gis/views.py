from django.shortcuts import render
from django.conf import settings
# from school_gis.models import InstMsbvee12Apr2020
# Create your views here.
def SchoolDash(request):
    # queryset = InstMsbvee12Apr2020.objects.all()
    context = {'site_url':settings.MY_SITE_URL}
    return render(request,'school_gis/school_base.html',context)
