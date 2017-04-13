from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^party_list/', views.PartyList.as_view(), name='party_list'),
    url(r'^project_list/', views.ProjectList.as_view(), name='project_list'),
    url(r'^parties/(?P<pk>[0-9]+)/$', views.PartyDetailView.as_view(), name='party_detail'),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^transactions/(?P<pk>[0-9]+)/$', views.TransactionDetailView.as_view(), name='transaction_detail'),
    url(r'^party/add/$', views.PartyCreate.as_view(), name='party_create'),
    url(r'^project/add/$', views.ProjectCreate.as_view(), name='project_create'),
    url(r'^transaction/add/$', views.TransactionCreate.as_view(), name='transaction_create'),
    url(r'^party/edit/(?P<pk>[0-9]+)/$', views.PartyUpdate.as_view(), name='party_update'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectUpdate.as_view(), name='project_update'),
    url(r'^transaction/(?P<pk>[0-9]+)/$', views.TransactionUpdate.as_view(), name='transaction_update'),
    url(r'^party/(?P<pk>[0-9]+)/delete/$', views.PartyDelete.as_view(), name='party_delete'),
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),
    url(r'^transaction/(?P<pk>[0-9]+)/delete/$', views.TransactionDelete.as_view(), name='transaction_delete'),
]
