from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import BuyerForm, InvoiceForm, InvoiceItemForm
from .models import Buyer, Invoice, InvoiceItem
# Create your views here.

class CreateBuyer(LoginRequiredMixin, CreateView):
    model = Buyer
    form_class = BuyerForm
    success_url = reverse_lazy('billing:list_buyers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = 'Add'
        return context


class UpdateBuyer(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Buyer
    form_class = BuyerForm
    success_url = reverse_lazy('billing:list_buyers')

    def get_object(self):
        return Buyer.objects.get(pk=self.kwargs['pk'])
    
    def test_func(self):
        return self.get_object().user == self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = 'Update'
        return context
    

class ListBuyers(LoginRequiredMixin, ListView):
    model = Buyer

    def get_queryset(self):
        return Buyer.objects.filter(user=self.request.user)
    

class DeleteBuyer(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Buyer
    success_url = reverse_lazy('billing:list_buyers')

    def test_func(self):
        return self.get_object().user == self.request.user
    

class CreateInvoice(LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    success_url = reverse_lazy('billing:list_invoices')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = 'Create'
        return context
    

class UpdateInvoice(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Invoice
    form_class = InvoiceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_object(self):
        return Invoice.objects.get(pk=self.kwargs['pk'])

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = 'Update'
        return context
    
    def get_success_url(self):
        return reverse_lazy('billing:detail_invoice', kwargs={'pk': self.kwargs['pk']})
    

class DetailInvoice(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Invoice

    def get_object(self):
        return get_object_or_404(Invoice, pk=self.kwargs['pk'])

    def test_func(self):
        invoice = self.get_object()
        return invoice.user == self.request.user


class ListInvoices(LoginRequiredMixin, ListView):
    model = Invoice

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)


class DeleteInvoice(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Invoice
    success_url = reverse_lazy('billing:list_invoices')

    def test_func(self):
        return self.get_object().user == self.request.user


class CreateInvoiceItem(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = InvoiceItem
    form_class = InvoiceItemForm

    def get_invoice(self):
        if not hasattr(self, '_invoice'):
            self._invoice = get_object_or_404(Invoice, pk=self.kwargs['pk'])
        return self._invoice

    def form_valid(self, form):
        form.instance.invoice = self.get_invoice()
        return super().form_valid(form)
    
    def test_func(self):
        return self.get_invoice().user == self.request.user

    def get_success_url(self):
        return reverse('billing:detail_invoice', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = 'Create'
        return context


class UpdateInvoiceItem(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = InvoiceItem
    form_class = InvoiceItemForm

    def get_invoice(self):
        if not hasattr(self, '_invoice'):
            item = get_object_or_404(InvoiceItem, pk=self.kwargs['pk'])
            self._invoice = item.invoice
        return self._invoice

    def test_func(self):
        return self.get_invoice().user == self.request.user

    def get_success_url(self):
        return reverse('billing:detail_invoice', kwargs={'pk': self.get_invoice().pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = 'Update'
        return context
    

class DeleteInvoiceItem(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = InvoiceItem

    def get_object(self):
        if not hasattr(self, '_object'):
            self._object = get_object_or_404(InvoiceItem, pk=self.kwargs['pk'])
        return self._object
    
    def get_invoice(self):
        return self.get_object().invoice
    
    def test_func(self):
        return self.get_invoice().user == self.request.user
    
    def get_success_url(self):
        return reverse('billing:detail_invoice', kwargs={'pk': self.get_invoice().pk})