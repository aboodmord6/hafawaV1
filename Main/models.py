
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None , **extra_fields):
        if not email:
            raise ValueError('Users must have a Email Address')
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password ):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    cp =  models.CharField(max_length=4) 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)  
    is_visitor = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
     


class AppAssets(models.Model):
    img = models.ImageField(upload_to='app/assets'  ,default='app/assets/banner.png' , null=False )