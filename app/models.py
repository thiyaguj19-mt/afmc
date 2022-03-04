from django.db import models
from datetime import datetime

# Create your models here.
class Volunteer(models.Model):

    first_name = models.CharField(max_length=100, help_text="enter first name")
    last_name = models.CharField(max_length=100, help_text="enter last name")
    email = models.EmailField(max_length=100, help_text="enter email")
    phone = models.CharField(max_length=100, help_text="enter phone number")
    V_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=20, choices=V_STATUS, default='Active')

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.status}'

class Provider(models.Model):

    first_name = models.CharField(max_length=100, help_text="enter first name")
    middle_name = models.CharField(max_length=100, help_text="enter middle name", blank=True)
    last_name = models.CharField(max_length=100, help_text="enter last name")
    email = models.EmailField(max_length=100, help_text="enter email")
    phone = models.CharField(max_length=20, help_text="enter phone number")
    TYPES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
    ]
    type = models.CharField(max_length=10, choices=TYPES, default='Doctor')
    license_number = models.CharField(max_length=20, help_text="enter license numbers", blank=True)
    P_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=20, choices=P_STATUS, default='Active')

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'

class Activities(models.Model):

    name = models.CharField(max_length=100, help_text="activity name")
    description = models.TextField(max_length=600, help_text="activity description")
    assigned_to = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, null=True, blank=True)
    TASK_STATUS = [
        ('backlog', 'backlog'),
        ('assigned', 'assigned'),
        ('in_progress', 'in_progress'),
        ('in_review', 'in_review'),
        ('completed', 'completed'),
    ]
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='backlog')
    start_date = models.DateField(help_text = 'enter start date',  null=True, blank=True)
    end_date = models.DateField(help_text = 'enter completed date', null=True, blank=True)

    def __str__(self):
        return f'Task Name - {self.name} | Task Status - {self.status} | Assigned To - {self.assigned_to}'

class Credentialing(models.Model):

    TYPES = [
        ('Intial', 'Intial'),
        ('Reappointment', 'Reappointment'),
    ]
    type = models.CharField(max_length=20, choices=TYPES)
    start_date = models.DateField(help_text = 'enter start date')
    end_date = models.DateField(help_text = 'enter completed date', blank=True)
    year = models.IntegerField(help_text = 'enter year of Credentialing', default=datetime.now().year)
    C_STATUS = [
        ('backlog', 'backlog'),
        ('assigned', 'assigned'),
        ('in_progress', 'in_progress'),
        ('in_review', 'in_review'),
        ('completed', 'completed'),
    ]
    status = models.CharField(max_length=20, choices=C_STATUS, default='backlog')
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    license_duedate = models.DateField(help_text = 'enter start date', null=True, blank=True)
    remarks = models.TextField(max_length=600, help_text="remarks/comments", blank=True)
    peer_reviewer_1 = models.CharField(max_length=100, help_text="enter peer review email address", blank=True)
    peer_reviewer_2 = models.CharField(max_length=100, help_text="enter peer review email address", blank=True)
    peer_reviewer_3 = models.CharField(max_length=100, help_text="enter peer review email address", blank=True)
