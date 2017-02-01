from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.core_list, name='core_list'),
    url(r'^parties/create/', views.parties_create_or_update),
    url(r'^projects/create/', views.projects_create_or_update),
    url(r'^transactions/create/', views.transactions_create_or_update),
    url(r'^parties/(?P<id>\d+)/$', views.parties_detail, name='party_detail'),
    url(r'^projects/(?P<id>\d+)/$', views.projects_detail, name='project_detail'),
    url(r'^transactions/(?P<id>\d+)/$', views.transactions_detail, name='transaction_detail'),
    url(r'^parties/(?P<id>\d+)/edit/$', views.parties_create_or_update),
    url(r'^projects/(?P<id>\d+)/edit/$', views.projects_create_or_update),
    url(r'^transactions/(?P<id>\d+)/edit/$', views.transactions_create_or_update),
    url(r'^parties/(?P<id>\d+)/delete/', views.parties_delete),
    url(r'^projects/(?P<id>\d+)/delete/', views.projects_delete),
    url(r'^transactions/(?P<id>\d+)/delete/', views.transactions_delete),
]
