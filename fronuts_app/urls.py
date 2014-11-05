from django.conf.urls import url

from fronuts_app import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^register_fronut/$', views.register_fronut, name='register_fronut')
]