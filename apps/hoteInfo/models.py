from django.db import models

# Create your models here.
class HotelInfo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.title
    

class Sidebar(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)

    def __str__(self):
        return self.title
    

class NewSteller(models.Model):
    email = models.CharField(max_length=252)

    def __str__(self):
        return self.email
    

class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    

class TeamModel(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=150)

    def __str__(self):
        return self.name