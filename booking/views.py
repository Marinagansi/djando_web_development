from ast import Store
from django.shortcuts import render,redirect
from store.models import Cloths
from booking.forms import BookedForm,BookingUpdateForm
from booking.models import Booking

# Create your views here.
# def booking(request,p_id):
#     print(request)
#     if request.method=="POST":
#         form=BookedForm(request.POST)
#         form.save()
#         return redirect ('home')
              
#     else:
#         form=BookedForm()
    
#     book=Cloths.objects.get(cloths_id=p_id)
#     return render(request,"booking/booking_form.html",{'book':book})

# def finalbooking(request): 
#     print(request)
#     if request.method=="POST":
#         form=BookedForm(request.POST)
#         form.save()
#         return redirect ('home')
              
#     else:
#         form=BookedForm()
    
#     return render(request,"booking/booking_form.html")


def booking_pannel(request):
    print(request)

   # customers=Room.objects.raw('select * from customer')
    books=Booking.objects.all

    return render(request,"booking/booking_pannel.html",{'books':books})

def edit(request,p_id):
    books=Booking.objects.get(booking_id=p_id)
    return render (request,"booking/booking_edit.html",{'books':books})

def book_update(request,p_id):
    #data verification
   
    print(request.POST)
    books=Booking.objects.get(booking_id=p_id)
    #bind data in form with instance of customer
    form = BookedForm(request.POST, instance=books)
    if form.is_valid():
        try:
            form.save()
            return redirect("/home")
        except:
            print("validation false")

    return render(request,"booking/booking_edit.html",{'books':books})

def delete(request,p_id):
    
    books=Booking.objects.get(booking_id=p_id)
    books.delete()
    return redirect("/c_pannel")
