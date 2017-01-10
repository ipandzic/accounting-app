from django import forms

from .models import Project, Party, Transaction


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "is_internal",
            "is_active"
        ]


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = [
            "name",
            "is_domestic",
            "vat_ptc",
            "is_active",
            "projects"
        ]


class TransactionForm(forms.ModelForm):
    class Meta:
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
