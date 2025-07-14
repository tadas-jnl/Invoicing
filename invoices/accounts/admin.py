from django.contrib import admin
from .models import User, CompanyProfile, IndividualProfile, BankAccount

# Register your models here.


admin.site.register(User)
admin.site.register(CompanyProfile)
admin.site.register(IndividualProfile)
admin.site.register(BankAccount)