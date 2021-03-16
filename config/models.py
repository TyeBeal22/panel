from django.db import models

# Create your models here.
class Setting(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=18)
    address = models.TextField()
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    about_us =models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
