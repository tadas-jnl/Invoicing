from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import BuyerForm, InvoiceForm
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
    success_url = '/'

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
    success_url = reverse_lazy('billing:list_invoices')

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
    

class ListInvoices(LoginRequiredMixin, ListView):
    model = Invoice

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)


class DeleteInvoice(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Invoice
    success_url = reverse_lazy('billing:list_invoices')

    def test_func(self):
        return self.get_object().user == self.request.user


