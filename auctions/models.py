from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class Listing(models.Model):

    Categories = [
        ('Tech', 'Tech'),
        ('House', 'House'),
        ('Kitchen', 'Kitchen'),
        ('Sport', 'Sport'),
        ('Cars', 'Cars'),
        ('Health', 'Health'),
        ('Food&Beverage', 'Food&Beverage'),
        ('Fashion', 'Fashion'),
    ]

    User     = models.ForeignKey(User, on_delete=models.PROTECT)
    Title    = models.CharField(max_length=50)
    Image    = models.ImageField(upload_to = 'auctions/static/media')
    Details  = models.TextField(blank=True)
    Price    = models.FloatField()
    Category = models.CharField(max_length=20, choices=Categories, null=True, blank=True)

    def __str__(self):
        return self.Title


class Bid(models.Model):
    Listing      = models.ForeignKey(Listing, on_delete=models.CASCADE)
    User         = models.ForeignKey(User, on_delete=models.PROTECT)
    Current_Bid  = models.FloatField(null=True)

    def __str__(self):
        return (f"{self.Listing} {self.Current_Bid}")




class Comment(models.Model):
    User    = models.ForeignKey(User, on_delete=models.PROTECT)
    Listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    Comment = models.TextField()

    def __str__(self):
        return (f"{self.User} {self.Listing}")



class Wishlist(models.Model):
    User    = models.ForeignKey(User, on_delete=models.CASCADE)
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.User} {self.Listing}")

