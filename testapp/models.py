from django.db import models
from rest_framework import serializers
# Create your models here.

class carModel(models.Model):
    carname = models.CharField(max_length=100)
    price = models.IntegerField()
     
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = carModel
        fields = "__all__"