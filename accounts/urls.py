from django.urls import path,include
from .import views

urlpatterns = [
    path('login',views.LoginPage,name="login"),
    path('register',views.RegisterPage,name='register'),
    path('logout',views.LogoutPage,name='logout'),
    path('dashboard',views.DashboardPage,name='dashboard'),


    
]
