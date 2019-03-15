from django.conf.urls import  url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^today/$', views.profile,name='profile'),
]