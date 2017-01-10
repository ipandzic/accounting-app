from django.conf.urls import url

from .views import (
    core_list,
    projects_create,
    parties_create,
    transactions_create,
    projects_detail,
    parties_detail,
    transactions_detail,
    projects_update,
    parties_update,
    transactions_update,
    projects_delete,
    parties_delete,
    transactions_delete,
    )

urlpatterns = [
    url(r'^$', core_list, name='core_list'),
    url(r'^parties/create/', parties_create),
    url(r'^projects/create/', projects_create),
    url(r'^transactions/create/', transactions_create),
    url(r'^parties/(?P<id>\d+)/$', parties_detail, name='party_detail'),
    url(r'^projects/(?P<id>\d+)/$', projects_detail, name='project_detail'),
    url(r'^transactions/(?P<id>\d+)/$', transactions_detail, name='transaction_detail'),
    url(r'^parties/(?P<id>\d+)/edit/$', parties_update, name='party_update'),
    url(r'^projects/(?P<id>\d+)/edit/$', projects_update, name='project_update'),
    url(r'^transactions/(?P<id>\d+)/edit/$', transactions_update, name='transaction_update'),
    url(r'^parties/(?P<id>\d+)/delete/', parties_delete),
    url(r'^projects/(?P<id>\d+)/delete/', projects_delete),
    url(r'^transactions/(?P<id>\d+)/delete/', transactions_delete),
]
