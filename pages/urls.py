from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.HomePage,name="home"),
    # path('cars',views.CarsPage,name="cars"),
    path('about',views.AboutPage,name="about"),
    path('services',views.ServicesPage,name="services"),
    path('contect',views.ContectPage,name="contect"),


]
