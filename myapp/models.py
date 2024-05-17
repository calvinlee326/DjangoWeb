from django.db import models
from unicodedata import name


# Create your models here.

class MenuCategory(models.Model):
    menu_category = models.CharField(max_length=200)

class Menu(models.Model):
    itemname = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, 
                                    related_name="category_name")

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time")

class Reservation(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

