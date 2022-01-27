from django.shortcuts import render,redirect
from store.forms import StoreForm
from store.models import Cloths
from django.contrib import messages

from booking.forms import BookedForm

# Create your views here.
def storeform(request):
    print(request.FILES)
    if request.method=="POST":
        stores=StoreForm(request.POST,request.FILES)
        stores.save()
        messages.success(request,"Add successfully")
          
        return redirect ("/cloth_pannel")
        

    else:
        stores=StoreForm()
     
    return render (request,"cloth/cloth_form.html",{'stores':stores})

def stores(request):
    
    print(request)

   # customers=Room.objects.raw('select * from customer')
    cloths=Cloths.objects.all

    return render(request,"store/store.html",{'cloths':cloths})


def cloths(request):
    
    print(request)

   # customers=Room.objects.raw('select * from customer')
    cloths=Cloths.objects.all

    return render(request,"cloth/cloth_pannel.html",{'cloths':cloths})

def edit(request,p_id):
    cloths=Cloths.objects.get(cloths_id=p_id)
    return render (request,"adminn/edit.html",{'cloths':cloths})


def update(request,p_id):
    #data verification
    cloths=Cloths.objects.get(cloths_id=p_id)
    #bind data in form with instance of customer
    form = StoreForm(request.POST, instance=cloths)
    if form.is_valid():
        try:
            form.save()
            return redirect("/cloth_pannel")
        except:
            print("validation false")
    return render(request,"adminn/edit.html",{'cloths':cloths})



def delete(request,p_id):
    
    cloths=Cloths.objects.get(cloths_id=p_id)
    cloths.delete()
    return redirect("/cloth_pannel")
  
def adminn(request):
    return render(request, "adminn/admin.html")


#book_form 
def cloth_details(request,p_id):
    print(request)
    if request.method=="POST":
        form=BookedForm(request.POST)
        form.save()
        return redirect ('/home')
              
    else:
        form=BookedForm()
    
    book=Cloths.objects.get(cloths_id=p_id)
    return render(request,"booking/booking_form.html",{'book':book})