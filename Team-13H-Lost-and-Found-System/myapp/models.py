from django.db import models

# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, unique= True)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "users"