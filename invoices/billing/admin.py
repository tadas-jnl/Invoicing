from django.contrib import admin
from .models import Buyer, Invoice, InvoiceItem

# Register your models here.

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ['number', 'buyer', 'issue_date', 'due_date', 'total']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Buyer)