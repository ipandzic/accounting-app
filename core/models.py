from __future__ import unicode_literals
from decimal import Decimal
import datetime
from datetime import date, timedelta
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

def get_first_day(dt, d_years=0, d_months=0):
	# d_years, d_months are "deltas" to apply to dt
	y, m = dt.year + d_years, dt.month + d_months
	a, m = divmod(m-1, 12)
	return date(y+a, m+1, 1)

def get_last_day(dt):
	return get_first_day(dt, 0, 1) + timedelta(-1)




class Project(models.Model):
	'''Describes a project that transactions, 
	clients, or people relate to.'''
	name = models.CharField(max_length=1024)
	is_internal = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

class Party(models.Model):
	'''represents an entity which paid the company, 
	or which was paid by the company. 
	'''

	name = models.CharField(max_length=1024)
	is_domestic = models.BooleanField(default=True)
	vat_ptc = models.IntegerField(
		default=25, validators=[MaxValueValidator(50), MinValueValidator(0)]
		)
	#projects = models.ManyToManyField()
	is_active = models.BooleanField(default=False)

class Transaction(models.Model):
	'''Represents any financial transaction 
	between a company and some party.
	'''
	party = models.ForeignKey(Party)

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

	#projects = models.ManyToManyField()

	#start_date = models.DateField(_("Date"), default=get_first_day(date))
	
	#end_date = models.DateField(_("Date"), default=get_last_day(date))
	
	#invoice_date = models.DateField(_("Date"), default=date.today())
	
	invoice_amount = models.DecimalField(max_digits=8, decimal_places=2)
	

	'''
	def vat_ammount(self, invoice_amount, )

	vat_ammount = models.DecimalField(
		max_digits=8, invoice_amount * party.vat_pct
		) 
	'''
	

	#party.invoice_pct => party.vat_pct
	
	settlement_date = models.DateField(null=True)
	
	settlement_ammount = models.DateField(default=0.00)
	
	adjustment = models.DateField(default=0.00)
	
	description = models.CharField(max_length=1024, default='')
	
	comments = models.TextField(default='')