from django.conf.urls import url
from . import views

app_name = 'API'

urlpatterns = [
    url(r'^party/$', views.PartyListAPIView.as_view(), name='party_list'),
    url(r'^party/create$', views.PartyCreateAPIView.as_view(), name='party_create'),
    url(r'^party/(?P<pk>[0-9]+)$', views.PartyDetailAPIView.as_view(), name='party_detail'),
    url(r'^party/(?P<pk>[0-9]+)/edit$', views.PartyUpdateAPIView.as_view(), name='party_update'),
    url(r'^party/(?P<pk>[0-9]+)/delete$', views.PartyDeleteAPIView.as_view(), name='party_delete'),
    url(r'^project/$', views.ProjectListAPIView.as_view(), name='project_list'),
    url(r'^project/create$', views.ProjectCreateAPIView.as_view(), name='project_create'),
    url(r'^project/(?P<pk>[0-9]+)$', views.ProjectDetailAPIView.as_view(), name='project_detail'),
    url(r'^project/(?P<pk>[0-9]+)/edit$', views.ProjectUpdateAPIView.as_view(), name='project_update'),
    url(r'^project/(?P<pk>[0-9]+)/delete$', views.ProjectDeleteAPIView.as_view(), name='project_delete'),
    url(r'^transaction/$', views.TransactionListAPIView.as_view(), name='transaction_list'),
    url(r'^transaction/create$', views.TransactionCreateAPIView.as_view(), name='transaction_create'),
    url(r'^transaction/(?P<pk>[0-9]+)$', views.TransactionDetailAPIView.as_view(), name='transaction_detail'),
    url(r'^transaction/(?P<pk>[0-9]+)/edit$', views.TransactionUpdateAPIView.as_view(), name='transaction_update'),
    url(r'^transaction/(?P<pk>[0-9]+)/delete$', views.TransactionDeleteAPIView.as_view(), name='transaction_delete'),
]
