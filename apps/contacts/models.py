from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(blank=False, max_length=50)
    phone = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
