from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=200)
    address = models.TextField()
    profession = models.CharField(max_length=200)
    tel_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)
    
    
    def __str__(self):
        return self.name
    