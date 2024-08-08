from django.db import models

class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.email
