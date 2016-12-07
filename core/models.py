from __future__ import unicode_literals
from django.db import models

from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.timezone import datetime, now
import calendar

# Create your models here.

def calculate_ammount(invoice_amount, vat_ptc):
	return int(invoice_amount) * float(vat_ptc)

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
	#	return self.party

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
	Transaction_type = models.CharField(
		max_length=1, default=1, 
		choices=TYPE_CHOICES
		)

	projects = models.ManyToManyField(Project, blank=True)

	def first_day_of_month():
		date = datetime.now()
		year, month = date.year, date.month
		return str(year) + '-' + str(month) + '-01'

	def last_day_of_month():
		date = datetime.now()
		year, month = date.year, date.month
		monthrange = calendar.monthrange(year, month)
		return str(year) + '-' + str(month) + '-' + str(monthrange[1])

	start_date = models.DateField(_("Start date"), default=first_day_of_month)
	
	end_date = models.DateField(_("End date"), default=last_day_of_month)
	
	invoice_date = models.DateField(_("Invoice date"), default=datetime.now)
	
	invoice_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)

	vat_ammount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)

	settlement_date = models.DateField(null=True)
	
	settlement_ammount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
	
	adjustment = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	
	description = models.CharField(max_length=1024, default='')
	
	comments = models.TextField(default='')