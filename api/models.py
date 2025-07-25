# we import models from django.db
from django.db import models

# we create our models here.
class AfricanLeaders(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return f"The President {self.name} from {self.country}"
