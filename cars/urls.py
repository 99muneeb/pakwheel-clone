from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.CarsPage,name="car"),
    path('<int:id>',views.Car_detailPage,name='car_detail'),
    path('search',views.SearchPage,name='search'),
    
    
]
