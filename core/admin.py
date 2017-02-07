from django.contrib import admin

from .models import Party, Project, Transaction
# Register your models here.

admin.site.register(Party)
admin.site.register(Project)
admin.site.register(Transaction)
