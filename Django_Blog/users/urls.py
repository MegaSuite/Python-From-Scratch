'''set the url patterns for users'''

from django.urls import path

from django.contrib.auth import login

from . import views

urlpatterns = [
    # Login page
    path('login/', views.login_view, name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register'),

]