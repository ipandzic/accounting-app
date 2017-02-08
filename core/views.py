<<<<<<< HEAD
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Party, Project, Transaction


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


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'core/project_detail.html'


class TransactionDetailView(generic.DetailView):
    model = Transaction
    template_name = 'core/transaction_detail.html'


class PartyCreate(CreateView):
    model = Party
    fields = [
        "name",
        "is_domestic",
        "vat_ptc",
        "is_active",
        "projects"
    ]


class PartyUpdate(UpdateView):
    model = Party
    fields = [
        "name",
        "is_domestic",
        "vat_ptc",
        "is_active",
        "projects"
    ]

    def get_initial(self):
        initial = super(PartyUpdate, self).get_initial()
        return initial


class PartyDelete(DeleteView):
    model = Party
    success_url = reverse_lazy("core:home")


class ProjectCreate(CreateView):
    model = Project
    fields = [
        "name",
        "is_internal",
        "is_active"
    ]


class ProjectUpdate(UpdateView):
    model = Project
    fields = [
        "name",
        "is_internal",
        "is_active"
    ]


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy("core:home")


class TransactionCreate(CreateView):
    model = Transaction
    fields = [
        "party",
        "direction",
        "transaction_type",
        "projects",
        "start_date",
        "end_date",
        "invoice_date",
        "invoice_amount",
        "vat_ammount",
        "settlement_date",
        "settlement_ammount",
        "adjustment",
        "description",
        "comments"
        ]


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = [
        "party",
        "direction",
        "transaction_type",
        "projects",
        "start_date",
        "end_date",
        "invoice_date",
        "invoice_amount",
        "vat_ammount",
        "settlement_date",
        "settlement_ammount",
        "adjustment",
        "description",
        "comments"
        ]


class TransactionDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy("core:home")
