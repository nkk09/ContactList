from django.db import models

# Create your models here.
class Contact(models.Model):
    index = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sex = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True) 
    job_title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.TextField()
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
