from django.conf.urls import url
from . import views

app_name = 'API'

urlpatterns = [
    url(r'^party_list/', views.PartyListAPI.as_view()),
    url(r'^project_list/', views.ProjectListAPI.as_view()),
    url(r'^transaction_list/', views.TransactionListAPI.as_view()),
]
