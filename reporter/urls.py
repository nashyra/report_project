'''
Created on 1/8/2016

@author: nashyra
'''
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf.urls import url
from reporter.generic import GalletaCreate, GalletaListView, GalletaDeleteView,\
    GalletaEditView

urlpatterns = [
               url("create$", GalletaCreate.as_view(),
                   name="galleta_create"),
               url("list$", GalletaListView.as_view(),
                   name="galleta_list_view"),
               url("delete$", GalletaDeleteView.as_view(),
                   name="galleta_delete_view"),
               url("edit$", GalletaEditView.as_view(),
                   name="galleta_edit_view")
]