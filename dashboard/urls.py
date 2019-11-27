from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.Dashboard),
    url(r'census',views.Census),
    url(r'devplan',views.DP_2014_34),
    url(r'swm',views.SWM),
    url(r'water',views.Water),
    url(r'health',views.Health),
    url(r'transport',views.Transport),
    url(r'edu',views.Education),
    url(r'goamap',views.Goadashboards),
    url(r'iit',views.IITBombay),
    url(r'tdsc',views.tdsc),
    url(r'test_animesh',views.test_animesh),
    url(r'thakkar_buppa_yojana',views.tby),
    url(r'deonadi',views.deonadi),
    url(r'pwss',views.pwss),
    url(r'palgarh',views.palgarh),

    

]