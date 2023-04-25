from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='uploads/categories', blank=True)

    def __str__(self) -> str:
        return self.category_name
