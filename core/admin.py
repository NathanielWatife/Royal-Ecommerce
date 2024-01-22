from django.contrib import admin
from .models import UserProfile, Cart, CartItem, Product, ContactModel, NewsLetter

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(ContactModel)
admin.site.register(NewsLetter)