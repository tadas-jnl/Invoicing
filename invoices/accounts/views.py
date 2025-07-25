from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CompanyProfileForm, IndividualProfileForm, BankAccountForm
from .models import CompanyProfile, IndividualProfile, BankAccount, User

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')    
            return redirect('accounts:cprofile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class ProfileCreate(LoginRequiredMixin, CreateView):
    template_name = "accounts/cprofile.html"

    def get_form_class(self):
        return CompanyProfileForm if self.request.user.is_company else IndividualProfileForm

    def get(self, request, *args, **kwargs):
        profile_form = self.get_form_class()()
        bank_form = BankAccountForm()
        return render(request, self.template_name, {
            'profile_form': profile_form,
            'bank_form': bank_form
        })
    
    def post(self, request, *args, **kwargs):
        profile_form = self.get_form_class()(request.POST)
        bank_form = BankAccountForm(request.POST)
        if profile_form.is_valid() and bank_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            bank_account = bank_form.save(commit=False)
            bank_account.user = request.user
            bank_account.save()

            return redirect(self.get_success_url())
        return render(request, self.template_name, {
            'profile_form': profile_form,
            'bank_form': bank_form
        })


    def get_success_url(self):
        if self.request.user.is_company:
            return reverse('accounts:company_profile')
        else:
            return reverse('accounts:individual_profile')


class CompanyProfileDetail(LoginRequiredMixin, DetailView):
    model = CompanyProfile

    def get(self, request, *args, **kwargs):
        try:
            self.object=self.get_object()
        except CompanyProfile.DoesNotExist:
            return redirect(reverse('accounts:cprofile'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self):
        return CompanyProfile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [
            (field.verbose_name, 
             field.value_from_object(self.object) if field.value_from_object(self.object) is not None else "—")
            for field in self.object._meta.fields
            if field.name not in ['user', 'id']
        ]
        try:
            context['bank_account'] = BankAccount.objects.get(user=self.request.user)
        except BankAccount.DoesNotExist:
            context['bank_account'] = None
        return context
    
    
class IndividualProfileDetail(LoginRequiredMixin, DetailView):
    model = IndividualProfile

    def get(self, request, *args, **kwargs):
        try:
            self.object=self.get_object()
        except IndividualProfile.DoesNotExist:
            return redirect(reverse('accounts:cprofile'))
        context =self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self):
        return IndividualProfile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [
            (field.verbose_name, 
             field.value_from_object(self.object) if field.value_from_object(self.object) is not None else "—")
            for field in self.object._meta.fields
            if field.name not in ['user', 'id']
        ]
        try:
            context['bank_account'] = BankAccount.objects.get(user=self.request.user)
        except BankAccount.DoesNotExist:
            context['bank_account'] = None
        return context
    

class CompanyProfileUpdate(LoginRequiredMixin, UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    success_url = "/accounts/cprofile"

    def get_object(self):
        return CompanyProfile.objects.get(user=self.request.user)


class IndividualProfileUpdate(LoginRequiredMixin, UpdateView):
    model = IndividualProfile
    form_class = IndividualProfileForm
    success_url = "/accounts/iprofile"

    def get_object(self):
        return IndividualProfile.objects.get(user=self.request.user)
    

class BankAccountUpdateView(LoginRequiredMixin, UpdateView):
    model = BankAccount
    form_class = BankAccountForm

    def get_object(self):
        return BankAccount.objects.get(user=self.request.user)

    def get_success_url(self):
        return reverse('accounts:company_profile') if self.request.user.is_company else reverse('accounts:individual_profile')


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/'

    def test_func(self):
        return self.get_object() == self.request.user
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('confirm_text') != 'DELETE':
            return self.get(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)