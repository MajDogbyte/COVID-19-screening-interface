from django.conf import settings
from django.db import models

# TODO probably won't be needed once OAuth is set up
#  remember to generate migration if you do remove it
class C19APIPatientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='c19_api_patient_profile',
        on_delete=models.CASCADE)
    # Need for this might disappear once using NHS login
    patient_nhs_number = models.TextField()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Covid-19 API Patient Profile'
        verbose_name_plural = 'Covid-19 API Patient Profiles'
