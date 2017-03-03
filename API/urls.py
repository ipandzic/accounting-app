from django.conf.urls import url
from . import views

app_name = 'API'

urlpatterns = [
    url(r'^party/$', views.PartyListAPI.as_view()),
    url(r'^party/(?P<pk>[0-9]+)$', views.PartyDetailAPI.as_view()),
    url(r'^project/$', views.ProjectListAPI.as_view()),
    url(r'^project/(?P<pk>[0-9]+)$', views.ProjectDetailAPI.as_view()),
    url(r'^transaction/$', views.TransactionListAPI.as_view()),
    url(r'^transaction/(?P<pk>[0-9]+)$', views.TransactionDetailAPI.as_view()),
]
