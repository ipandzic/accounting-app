from django.contrib import admin

# Register your models here.
from .models import Project, Party, Transaction

admin.site.register(Project)
admin.site.register(Party)
admin.site.register(Transaction)
