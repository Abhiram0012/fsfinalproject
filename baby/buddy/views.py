from django.shortcuts import render

# Create your views here.
from .models import Booking

# from .models import products

def index(request):
    # render is used displaying dynamic content
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def events(request):
    return render(request,'events.html')

def rooms(request):
    return render(request,'rooms.html')

# def contact(request):
#     items=products.objects.all()
#     context={'products':items}
#     return render(request,'contact.html')

# def reservation(request):
#     return render(request,'reservation.html')


def reservation(request):
    if  request.method == "POST":
        username=request.POST['name']
        userphone=request.POST['phone']
        useremail=request.POST['email']
        # usertext=request.POST['utext']

        # usercheckin=request.POST['checkin']
        # usercheckout=request.POST['checkout']
        

        # print(username,userphone,useremail,usernote)

        record=Booking.objects.create(name=username,
                                      phone=userphone,
                                      email=useremail,
                                    #   utext=usertext
                                    )

                                    #   datein=usercheckin,
                                    #   dateout=usercheckout,
        
        record.save()

    else :
        return render (request,'reservation.html')
    
    return render (request,'reservation.html')