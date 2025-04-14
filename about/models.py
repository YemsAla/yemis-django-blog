from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)


 class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
        ordering = ["-updated_on"]
