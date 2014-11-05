from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.core.urlresolvers import reverse

from fronuts_app.models import User, Shop, Fronut
from fronuts_app.forms import RegisterFronutForm

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'fronuts_app/index.html'
#     context_object_name = 'fronuts_list'
#     register_fronut_form = RegisterFronutForm()
#     def get_queryset(self):
#         return Fronut.objects.order_by('-date')

def index(request):
    template = loader.get_template('fronuts_app/index.html')
    fronuts_list = Fronut.objects.order_by('-date')
    register_fronut_form = RegisterFronutForm()
    context = RequestContext(request, {
                                       'fronuts_list': fronuts_list,
                                       'register_fronut_form': register_fronut_form,
                                       })
    return HttpResponse(template.render(context))
    
def register_fronut(request):
    if request.POST:
        form_data = RegisterFronutForm(request.POST)
        if form_data.is_valid():
            new_fronut = form_data.save(commit=False)
            new_fronut.register_and_save()
    return HttpResponseRedirect(reverse('fronuts:index'))