from django.db import models

# Create your models here.

class Member_informaiton (models.Model):
    name = models.CharField(max_length = 100)
    email = models.TextField()
    birth = models.DateTimeField()

class Member(models.Model):
    email = models.TextField()
    member_id = models.TextField()
    join_date = models.DateTimeField()