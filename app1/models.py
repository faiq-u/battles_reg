from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class applicant(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='applicant_photos/')
    games = models.ManyToManyField(Game, related_name='applicants', blank=False)
    email = models.EmailField(unique = True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return (self.name)