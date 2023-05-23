from django.db import models

# Create your models here.
class ContactModel(models.Model):
    local = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.email} | {self.phone}'
    
    
class ContactModelForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.name} | {self.email}'