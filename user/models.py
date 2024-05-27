from django.db import models
# Create your models here.

# TODO: Implement soft-delete
class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)

    class Meta:
        db_table = "passengers"
        indexes = [models.Index(fields=["email"]), models.Index(fields=["created_at"])]

# TODO: Implement soft-delete
class Cab(models.Model):
        id = models.AutoField(primary_key=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        cab_identifier = models.CharField(max_length=20, null=False, blank=False, unique=True)
        cab_model = models.CharField(max_length=100, null=False, blank=False)
        is_available = models.BooleanField(default=True, null=False, blank=False)
        latitude = models.IntegerField(blank=False, null=False)
        longitude = models.IntegerField(null=False, blank=False)

        class Meta:
            db_table = "cabs"
            # TODO: Add index on location field for faster retrieval
        
        def to_dict(self):
             return {"id": self.id, "model": self.cab_model, "lat": self.latitude, "long": self.longitude, "cab_identifier": self.cab_identifier} 
             