from django.db import models

# Create your models here.
class Contact(models.Model):
    index = models.AutoField(primary_key=True)  # Index field
    user_id = models.CharField(max_length=200, unique=True)  # Unique User Id
    first_name = models.CharField(max_length=200)  # First Name
    last_name = models.CharField(max_length=200)  # Last Name
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])  # Sex
    email = models.EmailField(max_length=254)  # Email
    phone = models.CharField(max_length=20)  # Phone
    date_of_birth = models.DateField()  # Date of Birth
    job_title = models.CharField(max_length=200)  # Job Title
    city = models.CharField(max_length=200)  # City
    country = models.CharField(max_length=200)  # Country
    address = models.TextField()  # Address
    fees = models.DecimalField(max_digits=10, decimal_places=2)  # Fees
    combined = models.TextField()  # Combined field for any other data

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
