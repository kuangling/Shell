from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=200)
    age=models.CharField(max_length=10)
    sex=models.CharField(max_length=10)

    def __unicode__(self):
        return self.username
