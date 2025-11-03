from django.db import models


class Hotel(models.Model):
    HotelName = models.CharField(max_length=200,unique=True,null=False,blank=False)
    RoomAvilable=models.IntegerField(default=0)
    Location= models.CharField(max_length=200,null=False,blank=False)
    Rating = models.FloatField(max_length=0,default=5,null=False,blank=False)
    PricePer=models.IntegerField(default=0,null=False,blank=False)
    Status=models.BooleanField(default=True,null=False,blank=False)
    def __str__(self):
        return self.HotelName

class User(models.Model):
    UserName=models.CharField(max_length=200,null=False,blank=False)
    UserID=models.IntegerField(unique=True,null=False,blank=False)
    BookingCost=models.IntegerField(default=0,null=False,blank=False)
    BookingRoom=models.CharField(max_length=200,null=False,blank=False)
    Status=models.BooleanField(default=True,null=False,blank=False)
    def __str__(self):
        return self.UserName