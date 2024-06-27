# products/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserDetailsManager(BaseUserManager):
    def create_user(self, emp_name, password=None):
        if not emp_name:
            raise ValueError('The Employee Name is required')
        user = self.model(emp_name=emp_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emp_name, password):
        user = self.create_user(emp_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserDetails(AbstractBaseUser):
    emp_id = models.BigAutoField(primary_key=True)
    emp_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15)

    objects = UserDetailsManager()

    USERNAME_FIELD = 'emp_name'

    def __str__(self):
        return self.emp_name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    emp_id = models.BigIntegerField()
