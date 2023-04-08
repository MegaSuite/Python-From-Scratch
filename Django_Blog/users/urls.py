'''set the url patterns for users'''

from django.urls import path

from django.contrib.auth import login

from . import views

urlpatterns = [
    # Login page
    path(r'^login/$', views.login_view, name='login'),
    # Logout page
    path(r'^logout/$', views.logout_view, name='logout'),

]