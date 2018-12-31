from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.IntegerField()
    event = models.CharField(max_length=10)
    store = models.CharField(max_length=10)
    img_src = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
