from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('cart/', views.Cart, name="cart"),
	path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
	path('remove-cart/', views.remove_cart, name="remove_cart"),
	path('shop-grid/', views.shopGrid, name="shopGrid"),

	# registration
	path('register/', views.register, name="register"),
	path('login/', views.signIn, name='signin'),
    path('logout/', views.userLogout, name='userlogout'),
    path('profile/', views.userAccount, name='userAccount'),
]
