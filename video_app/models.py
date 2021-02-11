from django.db import models

# Create your models here.
class Expire(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    code=models.CharField(max_length=50)
