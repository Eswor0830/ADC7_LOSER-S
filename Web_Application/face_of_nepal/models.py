from django.db import models

# Create your models here.

class freelancerManager(models.Manager):
  pass


class Freelancer(models.Model):
    Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Description = models.TextField()
    objects=freelancerManager()


    def __str__(self):
     return f"My Name is{self.Name}. I am from {self.Address} any time contact me {self.Phone}"
