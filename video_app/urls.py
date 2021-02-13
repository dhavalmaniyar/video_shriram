from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('call',views.call,name='call'),
    path('link',views.expirelink,name='link'),
    path('check', views.check, name="check"),
    path('subscribe', views.subscribe,name='subscribe'),
]
