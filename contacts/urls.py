from django.urls import path,include
from .import views

urlpatterns = [
    path('inquiry',views.PageInquiry,name='inquiry')




    
]
