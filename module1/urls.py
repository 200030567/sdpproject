from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('/hello',hello,name='hello'),
    path('',newhomepage,name='homepage'),
    path('travelpackage',travelpackage,name='travelpackage'),
    path('print_to_console/',print_to_console,name="print_to_console"),
    path('print1/',print1,name="print1"),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date/',get_date,name='get_date'),
    path('myregisterpage/',myregisterpage,name='myregisterpage'),
    path('registerloginfunction',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('cars123/',cars123,name='cars123'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('login/', weatherlogic, name='login'),
    path('logout/',weatherlogic,name='logout'),
    path('signup/',weatherlogic,name='signup'),
]
