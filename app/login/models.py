from django.db.models import Model, CharField, EmailField, BooleanField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, username, email, password):
        try:
            x = Account.objects.filter(username=username).first()
        except x:
            raise ValueError("Username alreadu used")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.staff = True
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.staff = True
        user.admin = True
        return user


class Account(AbstractBaseUser):
    username = CharField("username", max_length=250, unique=True)
    email = EmailField("email", max_length=250)
    password = CharField("password", max_length=100)
    admin = BooleanField(default=False)
    staff = BooleanField(default=False)
    is_active = BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
