from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from . import views

app_name = 'API'

schema_view = get_swagger_view(
    title='Accounting API',)

urlpatterns = [
    url(r'^party/$', views.PartyListAPI.as_view()),
    url(r'^party/(?P<pk>[0-9]+)$', views.PartyDetailAPI.as_view()),
    url(r'^project/$', views.ProjectListAPI.as_view()),
    url(r'^project/(?P<pk>[0-9]+)$', views.ProjectDetailAPI.as_view()),
    url(r'^transaction/$', views.TransactionListAPI.as_view()),
    url(r'^transaction/(?P<pk>[0-9]+)$', views.TransactionDetailAPI.as_view()),
    url(r'^docs/$', schema_view),
]
