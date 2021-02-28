from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class User(PermissionsMixin, AbstractBaseUser):
    """
    This model shall be used to hold the records of all the users.
    This model will further be used as the AUTH_USER_MODEL
    ------------------------------------------------------------------------------------
    Note: The logic is that we are building a "Phone Number" based authentication system
    Note: We will consider the "id" of the record as the EMPLOYEE_ID
    """
    first_name = models.TextField(default="")
    last_name = models.TextField(default="")
    email = models.EmailField(null=True)
    phone_number = models.TextField(null=False, primary_key=True)
    account_created_on = models.DateTimeField(default=timezone.now)  # Timezone shall be Asia/Kolkata set in settings.py

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return "{0} {1} || {2}".format(self.first_name, self.last_name, self.phone_number)

    def get_username(self):
        """ Return the full name of the user """
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_phone_number(self):
        return self.phone_number


class PersonalInfo(models.Model):
    """
    This model will store all the information related to the user at personal level.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address = models.TextField(default="")
    sex = models.CharField(max_length=6)
    age = models.IntegerField(default=0)


class ProfessionalInfo(models.Model):
    """
    Professional information includes all the information related to the position held by the employee in the company
    that may be required by the company in the records.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pan_card_number = models.CharField(max_length=10)  # PAN card number has max length of 10 characters.
    position = models.TextField(null=False)
    salary = models.FloatField(default=0.0)  # Basic payment received by the employee
    perks = models.FloatField(default=0.0)  # Total Amount spent by the company on the employee to provide extra benefits
