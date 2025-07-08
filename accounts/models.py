# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail est requise.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [('H', 'Homme'), ('F', 'Femme')]

    email = models.EmailField(unique=True)
    first_name = models.CharField(_('Prénom'), max_length=30)
    last_name = models.CharField(_('Nom'), max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    matricule = models.CharField(max_length=20, unique=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        if not self.matricule:
            self.matricule = self.generate_matricule()
        super().save(*args, **kwargs)

    def generate_matricule(self):
        today = timezone.now()
        year = today.strftime("%y")  # ex: 25
        month = today.strftime("%m")  # ex: 07
        count = CustomUser.objects.filter(date_joined__month=today.month).count() + 1

        count_format = f"{count:02}" if count < 100 else f"{count:03}"
        prefix = self.gender.upper()
        return f"{prefix}{count_format}{month}{year}"
    def get_fields(cls):
        return [field.name for field in cls._meta.fields]