from django.db import models

class Registration(models.Model):
    class Meta:
        verbose_name = "Registration"
        verbose_name_plural = "Registration"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=10, unique=True)
    canceled = models.BooleanField(default=False)
