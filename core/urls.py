from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact/', views.contact, name="contact"),
	path('cart/', views.Cart, name="cart"),
	path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
	path('remove-cart/', views.remove_cart, name="remove_cart"),
	path('shop-grid/', views.shopGrid, name="shopGrid"),	
	path('newsletter/', views.newsLetter, name="newsletter"),
	path('blog-single/', views.blog_single, name="blog-single"),

	# registration
	path('register/', views.register, name="register"),
	path('login/', views.signIn, name='signin'),
    path('logout/', views.userLogout, name='userlogout'),
    path('profile/', views.userAccount, name='userAccount'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),  
]
