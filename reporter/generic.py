'''
Created on 1/8/2016

@author: nashyra
'''

from __future__ import unicode_literals

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from reporter.models import Galletas
from django.contrib.messages.api import success

from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.db.models.query import QuerySet
from django.utils import timezone

class GalletaCreate(CreateView):
    model = Galletas
    fields = '__all__'
    success_url = "/"
    

class GalletaListView(ListView):
    model = Galletas
    
    def get_queryset(self):
        queryset = ListView.get_queryset(self)
        queryset = queryset.filter(cantidad__gte=5)
        return queryset
    
    def get_context_data(self, **kwargs):
        contex = ListView.get_context_data(self, **kwargs)
        contex['datetime'] = timezone.now()
        
        return contex

class GalletaDeleteView(DeleteView):
    model=Galletas
    fields= '__all__'
    success_url = reverse_lazy('galletas_list')
    
class GalletaEditView(UpdateView):
    model = Galletas 
    fields = '__all__'
    success_url = reverse_lazy('galletas_list')
    
    
    
