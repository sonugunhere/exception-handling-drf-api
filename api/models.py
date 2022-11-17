from django.db import models

# task -- create event upcoming and due event api
class AppointmentSchedule(models.Model):
    customer_name = models.CharField(max_length=40)
    appointment_date = models.DateTimeField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name

    
