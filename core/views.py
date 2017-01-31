from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProjectForm, PartyForm, TransactionForm
from .models import Project, Party, Transaction
# Create your views here.


def core_list(request):
    queryset_project = Project.objects.all()
    queryset_party = Party.objects.all()
    queryset_transaction = Transaction.objects.all()
    context = {
        "project_list": queryset_project,
        "party_list": queryset_party,
        "transaction_list": queryset_transaction,
        "title": "List"
    }
    return render(request, "list.html", context)


def parties_create_or_update(request, id=None):
    if id is not None:
        instance = get_object_or_404(Party, id=id)
        form = PartyForm(request.POST or None, instance=instance)
    else:
        form = PartyForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        return redirect("core_list")
    context = {"form": form}
    if id is not None:
        context["title"] = instance.name
        context["instance"] = instance
    return render(request, "party_form.html", context)


def projects_create_or_update(request, id=None):
    if id is not None:
        instance = get_object_or_404(Project, id=id)
        form = ProjectForm(request.POST or None, instance=instance)
    else:
        form = ProjectForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect("core_list")
    context = {"form": form}
    if id is not None:
        context["title"] = instance.name
        context["instance"] = instance
    return render(request, "project_form.html", context)


def transactions_create_or_update(request, id=None):
    if id is not None:
        instance = get_object_or_404(Transaction, id=id)
        form = TransactionForm(request.POST or None, instance=instance)
    else:
        form = TransactionForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect("core_list")
    context = {"form": form}
    if id is not None:
        context["title"] = instance.comments
        context["instance"] = instance
    return render(request, "transaction_form.html", context)


def parties_detail(request, id):
    instance = get_object_or_404(Party, id=id)
    context = {
        "title": instance.name,
        "id": instance.id,
        "instance": instance,
    }
    return render(request, "party_detail.html", context)


def projects_detail(request, id):
    instance = get_object_or_404(Project, id=id)
    context = {
        "title": instance.name,
        "id": instance.id,
        "instance": instance,
    }
    return render(request, "project_detail.html", context)


def transactions_detail(request, id):
    instance = get_object_or_404(Transaction, id=id)
    context = {
        "title": str(instance.party) + " - " + str(instance.comments),
        "instance": instance,
    }
    return render(request, "transaction_detail.html", context)


def parties_delete(request, id=None):
    instance = get_object_or_404(Party, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("core_list")


def projects_delete(request, id=None):
    instance = get_object_or_404(Project, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("core_list")


def transactions_delete(request, id=None):
    instance = get_object_or_404(Transaction, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("core_list")
