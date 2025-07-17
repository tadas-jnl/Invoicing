from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) #login with email
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_company = models.BooleanField(verbose_name='Are you a company or individual?', default=False) #True = company, False = individual
    is_staff = models.BooleanField(default=False) #allows login on admin site
    is_active = models.BooleanField(default=True) #allows soft ban without delete user
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def profile(self):
        if hasattr(self, 'individual_profile'):
            return self.individual_profile
        elif hasattr(self, 'company_profile'):
            return self.company_profile
        return None


class BaseProfile(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(verbose_name='Contact phone', max_length=15, null=True, blank=True)
    email = models.EmailField(verbose_name='Contact email', null=True, blank=True)
    web = models.CharField(verbose_name='Web site', max_length=100, null=True, blank=True)

    class Meta:
        abstract = True  #don't create separate db table for this. CompanyProfile and IndividualProfile will include fields of this class


class CompanyProfile(BaseProfile):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company_profile")
    name = models.CharField(verbose_name='Company name', max_length=200)
    company_code = models.CharField(verbose_name='Company code', max_length=20)
    vat_code = models.CharField(verbose_name='Tax payer code', max_length=20)

    def __str__(self):
        return self.name


class IndividualProfile(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='individual_profile')
    name = models.CharField(verbose_name='Full name', max_length=100)
    individual_code = models.CharField('Individual code', max_length=20, null=True, blank=True)
    vat_code = models.CharField(verbose_name='Tax payer code', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank')
    bank_name = models.CharField(verbose_name='Bank name', max_length=20, null=True, blank=True)
    swift = models.CharField(verbose_name='Bank code (SWIFT)', max_length=10, null=True, blank=True)
    iban = models.CharField(verbose_name='iban', max_length=20)

    def __str__(self):
        return f"Bank account for user: {self.user.email}"