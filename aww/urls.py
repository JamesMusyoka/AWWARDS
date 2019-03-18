from django.conf.urls import  url
from . import views

urlpatterns=[
    # url('^$', views.signup, name='signup'),
    url('^$',views.index,name = 'index'),
    url(r'^projects/',views.project, name='projects'),
    url(r'^profile/', views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project/$', views.new_project, name='new-project'),
    url(r'^rate/$', views.rate, name='rate'),
]

