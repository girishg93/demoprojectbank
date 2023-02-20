from django.db import models

class Register(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    cnfm_password=models.CharField(max_length=255)

    class Meta:
        verbose_name='Register'
        verbose_name_plural="Registrations"

    def __str__(self):
        return self.username
