'''
Created on 1/8/2016

@author: nashyra
'''

from __future__ import unicode_literals

from django.views.generic.edit import CreateView, DeleteView
from reporter.models import Galletas
from django.contrib.messages.api import success

from django.views.generic.list import ListView

class GalletaCreate(CreateView):
    model = Galletas
    fields = '__all__'
    success_url = "/"
    

class GalletaListView(ListView):

    model = Galletas
    

class GalletaDeleteView(DeleteView):
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(GalletaDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj
    
class GalletaEditView(EditView):
    model = Galletas 
    
    
