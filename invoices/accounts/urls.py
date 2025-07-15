from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.signup_view, name='sign_up'),
    path('profile/create/', views.ProfileCreate.as_view(), name='cprofile'),
    path('cprofile/', views.CompanyProfileDetail.as_view(), name='company_profile'),
    path('iprofile/', views.IndividualProfileDetail.as_view(), name='individual_profile'),
    path('cprofile/update/', views.CompanyProfileUpdate.as_view(), name='cprofile_update'),
    path('iprofile/update/', views.IndividualProfileUpdate.as_view(), name='iprofile_update'),
    path('profile/bank/', views.BankAccountUpdateView.as_view(), name='bank'),
]

