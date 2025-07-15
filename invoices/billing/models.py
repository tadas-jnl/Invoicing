from django.db import models
from django.conf import settings
from datetime import date
from decimal import Decimal


# Create your models here.

class Buyer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Buyer name", max_length=200)
    code = models.CharField(verbose_name="Buyer code", max_length=20)
    vat_code = models.CharField(verbose_name="Buyer tax payer code", max_length=20, null=True, blank=True)
    address = models.CharField(verbose_name="Buyer address", max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Buyer: { self.name }"

class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, verbose_name="Buyer", on_delete=models.SET_NULL, null=True, blank=True)
    number = models.IntegerField(verbose_name="Invoice number")
    series = models.CharField(verbose_name="Series", max_length=20)
    issue_date = models.DateField(verbose_name="Issue date", default=date.today)
    due_date = models.DateField(verbose_name="Due date")
    include_vat = models.BooleanField(verbose_name="VAT included", default=True)

    def __str__(self):
        return f"Invoice NO: { self.number } - Buyer: { self.buyer }"
    
    def subtotal(self):
        return sum( item.line_total() for item in self.items.all() )
    
    def vat_amount(self):
        if self.include_vat:
            return self.subtotal() * 21 / Decimal("100.00")
        return Decimal("0.00")

    def total(self):
        return self.subtotal() + self.vat_amount()
    

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Description", max_length=255)
    qty = models.DecimalField(verbose_name="Quantity", max_digits=10, decimal_places=2)
    units = models.CharField(verbose_name="Measurement units", max_length=20)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Invoice { self.invoice.number } item: { self.description }: { self.qty } { self.units } x { self.price } Eur"
    
    def line_total(self):
        return self.qty * self.price
    

