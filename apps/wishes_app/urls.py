from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^(\d+)$', views.show),
    url(r'^(\d+)/edit/', views.edit),
    url(r'^(\d+)/destroy/$', views.destroy),
    url(r'^(\d+)/grant/$', views.grant),
    url(r'^(\d+)/like/$', views.like),

    url(r'^create', views.create),
    url(r'^update', views.update),
    url(r'^new', views.new), 
    url(r'^stats', views.stats), 
    url(r'^$', views.index)
]
