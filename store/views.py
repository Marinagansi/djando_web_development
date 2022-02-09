from django.shortcuts import render,redirect
from store.forms import StoreForm
from store.models import Cloths
from booking.models import Booking
from customer.models import Customer
from django.contrib import messages
from django.core.mail import send_mail
from booking.forms import BookedForm

# Create your views here.
def storeform(request): 
    print(request.FILES)
    if request.method=="POST":
        stores=StoreForm(request.POST,request.FILES)
        stores.save()
        messages.success(request,"Add successfully")
          
        return redirect ("/store/cloth_pannel")
        

    else:
        stores=StoreForm()
     
    return render (request,"cloth/cloth_form.html",{'stores':stores})

def stores(request):
    
    print(request)
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*9
        print(offset)
    else:
        offset=0
        page=1

   # customers=Room.objects.raw('select * from customer')
    cloths=Cloths.objects.raw("select * from store limit 9 offset % s",[offset])
    pageItem=len(cloths)

    return render(request,"store/store.html",{'cloths':cloths,'page':page,'pageItem':pageItem})


def cloths(request):
    
    print(request)
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*1
        print(offset)
    else:
        offset=0
        page=1

   # customers=Room.objects.raw('select * from customer')
    cloths=Cloths.objects.raw("select * from store limit 1 offset % s",[offset])
    pageItem=len(cloths)
    booking_count=Booking.objects.count()
    customer_count=Customer.objects.count()
    cloths_count=Cloths.objects.count()
    return render(request,"cloth/cloth_pannel.html",{'cloths':cloths,'page':page,'pageItem':pageItem,'customer_count':customer_count,'booking_count':booking_count,'cloths_count':cloths_count})

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


#book_form for cloths
def cloth_details(request,p_id):
    print(request)
    if request.method=="POST":
        form=BookedForm(request.POST)
        if form.is_valid():
            try:

                form.save()
      
                b_email=request.POST['email']
                date=request.POST['start_date']
                days=request.POST['days']
       

                send_mail(
                    'STYLOOK',
                    'Clothes you have been hire has been register'+"\n"

                    'your hire date is'+ date +"\n"
                    'you have hire for'+days,
                    b_email,
                    ['gansimarina@gmail.com'],
                )
                messages.success(request,"your booking has been  registered check you email")
                return redirect ('/store/shop')
            except:
                print("error")
                

        
              
    else:
        form=BookedForm()
    
    book=Cloths.objects.get(cloths_id=p_id)
    cloths=Cloths.objects.raw('select * from store limit 5')
    return render(request,"booking/booking_form.html",{'form':form,'book':book,'cloths':cloths})

def search_cloth(request):
    if request.method=="POST":
        searched=request.POST['searched']
        venues = Cloths.objects.filter(cloths_name__icontains=searched)
        return render(request, "store/search.html",{'searched':searched,'venues':venues})
    else:
        return render(request, "store/search.html",{})
    