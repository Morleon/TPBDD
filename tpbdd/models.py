from django.db import models

# Create your models here.
class DatabaseData(models.Model):
	key = models.IntegerField()
	number = models.IntegerField()