from django.db import models
from user.models import Passenger, Cab

# Create your models here.
class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    cab_id = models.ForeignKey(Cab, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = "trips"
        indexes = [models.Index(fields=["is_completed"])]
