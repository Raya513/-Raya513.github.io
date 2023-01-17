from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    #password=models.CharField(max_length=12)
    phone=models.TextField()
    #date=models.DateField()
    item=models.CharField(max_length=122)
    quantity=models.TextField()
    
    def __str__(self):
        return self.name