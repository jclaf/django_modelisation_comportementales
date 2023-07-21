from django.db import models
from django.utils.translation import gettext_lazy as _
#from django.contrib.postgres.fields import ArrayField

# Create your models here.

"""
class Status(models.TextChoices):
    ACTIVATE = 'a', "Activate"
    DESACTIVATE = 'd', "Desactivate"
    
class Day(models.IntegerChoices):
    MONDAY = 0, _('Monday')
    TUESDAY = 1, _("Tuesday")
    WEDNESDAY = 2, _("Wednesday")
    THURSDAY = 3, _("Thursday")
    FRIDAY = 4, _("Friday")
    SATURDAY = 5, _("Saturday")
    SUNDAY = 6, _("Sunday")"""


  
class Filter(models.Model):
    name = models.CharField( max_length=65, unique=True)
    #status = models.CharField(verbose_name="Rule status", max_length=1, choices=Status.choices)
    days = models.CharField(verbose_name="Days status", max_length=100,blank=True)
    
    start_time = models.TimeField(verbose_name="Start time",null=True, blank=True)
    end_time = models.TimeField(verbose_name="End time",null=True, blank=True)
    #date = models.BooleanField("Add date", default=False)
    start_date = models.DateField(verbose_name="Start date",null=True, blank=True)
    end_date = models.DateField(verbose_name="End date",null=True, blank=True)
    
    
    os = models.CharField(max_length=50, blank=True)
    
    #mettre un moyen de choisir entre  ipv4 ou ipv6
    network = models.CharField(verbose_name='IP address', max_length=20, blank=True)
    subnet = models.CharField(verbose_name='Subnet',max_length=20, blank=True)
    router = models.CharField(verbose_name='Router', max_length=20, blank=True)
    DHCP = models.CharField(verbose_name="DHCP", max_length=20, blank=True)
    
    DNS = models.CharField(verbose_name="DNS", max_length=50, blank=True)
    
    BYOD = models.IntegerField(verbose_name="BYOD",null=True, blank=True)
    
    #extra_field = models.CharField(max_length=20, blank=True)
    def get_days_as_string(self):
        days_mapping = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday',
        }

        days_list = [days_mapping[int(day)] for day in self.days.split(",") if day.strip().isdigit()]
        return ", ".join(days_list)
    
    def __str__(self):
        return self.name
    


class Access(models.Model):
    
    #chaque utilisaateur a acces a tel service
    #verifier s'il est externe ou interne (AD ou autres)
    #
    def __str__(self):
        return self.name


class FilterExtra (models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    extra = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    DELETE = models.BooleanField(default=False)
    
    def __str__(self):
        return self.extra


# période de date
# période d'heure
# os différent 

