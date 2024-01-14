from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('shop-grid/', views.shopGrid, name="shopGrid"),

	# registration
	path('register/', views.register, name="register"),
	path('login/', views.signin, name='signin'),
    path('logout/', views.userLogout, name='userlogout'),
]
