from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from datetime import timedelta
from . managers import UserManager
from random import randint

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Эл. почта", unique=True, blank=False, null=False)
    full_name = models.CharField(verbose_name="ФИО", max_length=80)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return f'{self.full_name} ({self.email})'
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    
class PasswordResetCode(models.Model):
    email = models.EmailField(verbose_name="Эл. почта", blank=False, null=False)
    code = models.CharField(max_length=4)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at
    
    @classmethod
    def create_code(cls, email):
        cls.objects.filter(email=email).delete()

        return cls.objects.create(
            email=email,
            code=str(randint(1000, 9999)),
            expires_at=timezone.now() + timedelta(minutes=5)
        )
