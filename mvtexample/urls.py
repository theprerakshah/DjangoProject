
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from mvtexample import views



urlpatterns = [
  #path('admin/', admin.site.urls),
  path('index',views.index, name='index'),
  path('index2',views.index2, name='index2'),
  path('',views.eform, name='eform'),
  path('myform',views.myform, name='myform'),
 
    

]
