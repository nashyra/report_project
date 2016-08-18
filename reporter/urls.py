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
               url("delete/(?P<pk>\d+)$", GalletaDeleteView.as_view(),
                   name="galletas_confirm_delete"),
               url("update/(?P<pk>\d+)$", GalletaEditView.as_view(),
                   name="galletas_update")
]