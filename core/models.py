from __future__ import unicode_literals

import calendar

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import gettext as _

# Create your models here.


class Project(models.Model):
    """
    Describes a project that transactions, clients, or people relate to.
    """
    name = models.CharField(max_length=1024)
    is_internal = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Party(models.Model):
    """
    Represents an entity which paid the company, or which was paid by the company.
    """
    name = models.CharField(max_length=1024)
    is_domestic = models.BooleanField(default=True)
    vat_ptc = models.IntegerField(
        default=25, validators=[MaxValueValidator(50), MinValueValidator(0)])
    projects = models.ManyToManyField(Project, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
    Represents any financial transaction between a company and some party.
    """
    DIRECTION_CHOICES = (
        ('1', 'incoming'),
        ('2', 'outgoing')
        )
    TYPE_CHOICES = (
        ('1', 'invoice'),
        ('2', 'tax'),
        ('3', 'payroll'),
        ('4', 'profit'),
        ('5', 'adjustment')
        )

    def calculate_first_day_of_month():
        """Returns the first day of a given month."""
        date = datetime.now()
        return date.replace(day=1)

    def calculate_last_day_of_month():
        """Returns the last day of a given month."""
        date = datetime.now()
        return date.replace(day=calendar.monthrange(date.year, date.month)[1])

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    direction = models.CharField(max_length=1, default=1, choices=DIRECTION_CHOICES)
    transaction_type = models.CharField(max_length=1, default=1, choices=TYPE_CHOICES)
    projects = models.ManyToManyField(Project, blank=True)
    start_date = models.DateField(_("Start date"), default=calculate_first_day_of_month)
    end_date = models.DateField(_("End date"), default=calculate_last_day_of_month)
    invoice_date = models.DateField(_("Invoice date"), default=datetime.today)
    invoice_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    vat_ammount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    settlement_date = models.DateField(null=True, blank=True, default=None)
    settlement_ammount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    adjustment = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1024, default='')
    comments = models.TextField(default='')

    def __str__(self):
        return str(self.party) + ' - ' + self.description
