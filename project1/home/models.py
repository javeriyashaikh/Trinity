from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date= models.DateField()
    rollno = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name
