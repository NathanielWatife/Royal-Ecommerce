from django.db import models
from django.contrib.auth.models import User
from .choices import PRODUCT_CHOICES

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=PRODUCT_CHOICES)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    
    def __str__(self):
        return self.user
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.cart
	


# models class for contact page
class ContactModel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    message = models.TextField()
    
    def __str__(self):
        return self.email
    

class NewsLetter(models.Model):
    email = models.CharField(max_length=70, null=True, blank=True)
    
    def __str__(self):
        return self.email
	