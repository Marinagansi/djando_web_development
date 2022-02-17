from ast import Store
from django.shortcuts import render,redirect
from store.models import Cloths
from booking.forms import BookedForm,BookingUpdateForm
from booking.models import Booking
from customer.models import Customer
from django.contrib import messages
from authenticate import Authentication
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def booking_pannel(request):

    print(request)
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*2
        print(offset)
    else:
        offset=0
        page=1

    books=Booking.objects.raw("select * from booking limit 2 offset % s",[offset])
    pageItem=len(books)
    booking_count=Booking.objects.count()
    customer_count=Customer.objects.count()
    cloths_count=Cloths.objects.count()
    return render(request,"booking/booking_pannel.html",{'books':books,'page':page,'pageItem':pageItem,'customer_count':customer_count,'booking_count':booking_count,'cloths_count':cloths_count})



def edit(request,p_id):
    books=Booking.objects.get(booking_id=p_id)
    return render (request,"booking/booking_edit.html",{'books':books})

def book_update(request,p_id):
    #data verification
   
    print(request.POST)
    books=Booking.objects.get(booking_id=p_id)
    #bind data in form with instance of books
    form = BookedForm(request.POST, instance=books)
    if form.is_valid():
        try:
            form.save()
            messages.success(request,"data has been updated ")
            return redirect("/booking/booking_pannel")
        except:
            print("validation false")

    return render(request,"booking/booking_edit.html",{'books':books})

def delete(request,p_id):
    
    books=Booking.objects.get(booking_id=p_id)
    books.delete()
    messages.success(request,"data has been deleted")
    return redirect("/booking/booking_pannel")


def Userprofile(request,p_id):
    customers=Customer.objects.get(customer_id=p_id)
    booking=Booking.objects.filter(consumer_id=p_id)
    return render (request,"user_profile.html",{'customers':customers,'booking':booking})

