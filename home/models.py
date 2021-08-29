from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name