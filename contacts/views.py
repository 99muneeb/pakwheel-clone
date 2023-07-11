from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def PageInquiry(request):
    if request.method =='POST':
        car_id=request.POST['car_id']
        car_title=request.POST['car_title']
        user_id=request.POST['user_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made enquiry of this car')
                return redirect('/cars/'+car_id)



        connect=Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,email=email,phone=phone,message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New car Inquiry.',
            'You have a new Inquiry'+ car_title + '.Please check your dashboard',
            'muneeb9166@gmail.com',
            [admin_email],
            fail_silently=False,
)
        connect.save()
        messages.success(request,'Your request has been submitted')
        return redirect('/cars/'+car_id)
