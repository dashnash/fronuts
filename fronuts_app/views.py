from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

from fronuts_app.models import User, Shop, Fronut

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'fronuts_app/index.html'
    context_object_name = 'fronuts_list'
    
    def get_queryset(self):
        return Fronut.objects.order_by('-date')