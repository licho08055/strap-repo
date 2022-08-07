from django.db import models

# Create your models here.


class People(models.Model):
    user_id = models.IntegerField()
    friends_id = models.IntegerField()


class Planet(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    code = models.CharField(max_length=20)
    picture_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Character(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    picture_url = models.CharField(max_length=200)
    planet =  models.ForeignKey(Planet, on_delete=models.CASCADE)
    people = models.ManyToManyField(People)
    
    
    def __str__(self):
        return self.name