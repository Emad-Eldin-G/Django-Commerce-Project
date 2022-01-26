from http.client import MULTIPLE_CHOICES
from operator import truediv
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators


class User(AbstractUser):
    pass

class Listing(models.Model):

    Categories = [
        ('Tech', 'Tech'),
        ('House', 'House'),
        ('Kitchen', 'Kitchen'),
        ('Sport', 'Sport'),
    ]

    User     = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    Title    = models.CharField(max_length=50)
    Details  = models.TextField()
    Price    = models.FloatField()
    Category = models.CharField(max_length=20, choices=Categories, null=True, blank=True)

    def __str__(self):
        return self.Title
 

class User_Listing(models.Model):
    User    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    


class Bid(models.Model):
    Listing      = models.ForeignKey(Listing, on_delete=models.CASCADE)
    Previous_Bid = models.FloatField()
    Current_Bid  = models.FloatField()
    Active = models.BooleanField()

    def __str__(self):
        return self.Listing + self.Current_Bid




class Comment(models.Model):
    User    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    Listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    Comment = models.TextField()

    def __str__(self):
        return self.Listing + f"({self.Comment})"


class Wishlist(models.Model):
    User    = models.ForeignKey(User, on_delete=models.CASCADE)
    Listing = models.ForeignKey(Listing, on_delete=models.PROTECT)

    def __str__(self):
        return (f"{self.User} {self.Listing}")

