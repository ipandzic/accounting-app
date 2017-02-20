from django.views import generic
from django.core.urlresolvers import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Party, Project, Transaction
from .forms import PartyForm, ProjectForm, TransactionForm
from API.serializers import PartySerializer, ProjectSerializer, TransactionSerializer


class Home(generic.ListView):
    template_name = 'core/list.html'
    context_object_name = 'all_transactions'

    def get_queryset(self):
        return Transaction.objects.all()


class PartyList(generic.ListView):
    template_name = 'core/party_list.html'
    context_object_name = 'all_parties'

    def get_queryset(self):
        return Party.objects.all()


class ProjectList(generic.ListView):
    template_name = 'core/project_list.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()


class PartyDetailView(generic.DetailView):
    model = Party
    template_name = 'core/party_detail.html'
    form_class = PartyForm


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    form_class = ProjectForm


class TransactionDetailView(generic.DetailView):
    model = Transaction
    template_name = 'core/transaction_detail.html'
    form_class = TransactionForm


class PartyCreate(generic.CreateView):
    model = Party
    form_class = PartyForm


class ProjectCreate(generic.CreateView):
    model = Project
    form_class = ProjectForm


class TransactionCreate(generic.CreateView):
    model = Transaction
    form_class = TransactionForm


class PartyUpdate(generic.UpdateView):
    model = Party
    form_class = PartyForm


class ProjectUpdate(generic.UpdateView):
    model = Project
    form_class = ProjectForm


class TransactionUpdate(generic.UpdateView):
    model = Transaction
    form_class = TransactionForm


class PartyDelete(generic.DeleteView):
    model = Party
    success_url = reverse_lazy("core:party_list")


class ProjectDelete(generic.DeleteView):
    model = Project
    success_url = reverse_lazy("core:project_list")


class TransactionDelete(generic.DeleteView):
    model = Transaction
    success_url = reverse_lazy("core:home")


class PartyListAPI(APIView):
    def get(self, request):
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)


class ProjectListAPI(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class TransactionListAPI(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
