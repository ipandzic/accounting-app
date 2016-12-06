from __future__ import unicode_literals
from django.db import models

import datetime
from datetime import date, timedelta

from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from decimal import Decimal

from django.utils.timezone import datetime
import calendar

# Create your models here.

class Project(models.Model):
	'''Describes a project that transactions, 
	clients, or people relate to.'''
	def __str__(self):
		return self.name

	name = models.CharField(max_length=1024)
	is_internal = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)


class Party(models.Model):
	'''represents an entity which paid the company, 
	or which was paid by the company.'''
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "parties"

	name = models.CharField(max_length=1024)
	is_domestic = models.BooleanField(default=True)
	vat_ptc = models.IntegerField(
		default=25, validators=[MaxValueValidator(50), MinValueValidator(0)]
		)
	projects = models.ManyToManyField(Project)
	is_active = models.BooleanField(default=False)


class Transaction(models.Model):
	'''Represents any financial transaction 
	between a company and some party.'''
	#def __str__(self):
	#	return self.name

	def first_day_of_month(d):
		return date(d.year, d.month, 1)

	party = models.ForeignKey(Party, on_delete=models.CASCADE)

	DIRECTION_CHOICES = (
	('1','incoming'),
	('2','outgoing')
	)
	direction = models.CharField(
					max_length=1, default=1, 
					choices=DIRECTION_CHOICES
				)
	
	TYPE_CHOICES = (
	('1', 'invoice'),
	('2', 'tax'),
	('3', 'payroll'),
	('4', 'profit'),
	('5', 'adjustment')
	)
	type1 = models.CharField(
		max_length=1, default=1, 
		choices=TYPE_CHOICES
		)

	projects = models.ManyToManyField(Project, blank=True)

	today = datetime.today()
	year, month = today.year, today.month
	monthrange = calendar.monthrange(year, month)
	first_day_of_month = str(year) + '-' + str(month) + '-01'
	last_day_of_month = str(year) + '-' + str(month) + '-' + str(monthrange[1])

	start_date = models.DateField(_("Start date"), default=first_day_of_month)
	
	end_date = models.DateField(_("End date"), default=last_day_of_month)
	
	invoice_date = models.DateField(_("Invoice date"), default=today)
	
	invoice_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

	#total = invoice_amount * Party.vat_ptc
	vat_ammount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

	settlement_date = models.DateField(null=True)
	
	settlement_ammount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	
	adjustment = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	
	description = models.CharField(max_length=1024, default='')
	
	comments = models.TextField(default='')