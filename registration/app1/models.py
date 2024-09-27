from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import hashlib

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        # Manually hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = self.model(username=username, email=self.normalize_email(email))
        user.password = hashed_password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)  # Adjusted to accommodate the hash length
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def set_password_1(self, raw_password):
        # Manually hash the password using SHA-256
        self.password = hashlib.sha256(raw_password.encode('utf-8')).hexdigest()
        print("Setting the Password", self.password)

    def check_password_1(self, raw_password):
        # Verify the password using SHA-256
        hashed_pass = hashlib.sha256(raw_password.encode('utf-8')).hexdigest()
        print("In check Password User Password Hash: ",hashed_pass)
        print("In check Password Ownr Password Hash: ",self.password)
        return self.password == hashed_pass

    def save_user(self, *args, **kwargs):
        # if self._state.adding or 'password' in kwargs.get('update_fields', []):
        #     self.set_password_1(self.password)
        super(User, self).save(*args, **kwargs)
        print("Everything Done in the save_user function")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'app1_baseusers'
