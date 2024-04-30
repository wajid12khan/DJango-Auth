from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('home', views.home, name='home'),
    path('logout', views.pagelogout, name='logout'),


]
