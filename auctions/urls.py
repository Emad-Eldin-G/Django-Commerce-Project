from django.urls import path

from . import views

app_name = "commerce"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("commerce/<listing>", views.Listing_Page, name="listing"),
    path("New", views.new_listing, name="New"),
    path("Wishlist", views.wishlist, name="Wishlist"),

]
