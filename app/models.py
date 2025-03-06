from django.db import models
# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Mobile field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('role', 'admin')
        
        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    BLOOD = {
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
        
    }
    username = None
    image = models.ImageField(upload_to='users', null=True, blank=True, default='avatar.png')
    name = models.CharField(max_length=220)
    phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=220)
    facebook_page = models.URLField(default='')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "phone"
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-created_at', )
        verbose_name = ("User")
        verbose_name_plural = ("Users")



