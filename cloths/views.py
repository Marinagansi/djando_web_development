from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authenticate import Authentication
from cloths.forms import UserForm
from booking.models import Booking
from customer.models import Customer
from store.models import Cloths

# Create your views here.


def nav(request):
    return render(request,"nav.html")

def firstpage(request):
    return render(request,"firstpage.html")

@login_required(login_url='/login')
def admin2(request):
    booking_count=Booking.objects.count()
    customer_count=Customer.objects.count()
    cloths_count=Cloths.objects.count()
    return render(request,"adminn/admin2.html",{'booking_count':booking_count,'customer_count':customer_count,'cloths_count':cloths_count})




# @login_required(login_url='/customer/signin')
@Authentication.valid_user
def home(request):
    return render(request,"home.html")

def loginn(request):
    if request.method=='POST':
        customer_name=request.POST.get("customer_name")
        customer_password=request.POST.get("customer_pasword")

        # user=Registration.objects.get(customer_name=customer_name,customer_phone=customer_password)
        # if user is not None:
        

        user = authenticate(request, username=customer_name,password=customer_password)
      
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect ("/store/cloth_pannel")

        else:
            messages.info(request,'Invalid user')
    return render(request,"login.html")
   

def registration(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        psw=request.POST['psw']

        user=User.objects.create_user(username=name,email=email,password=psw)
        user.save()
        return redirect ("/store/cloth_pannel")
    
    return render(request,"registration.html")

def logout_page(request):
    logout(request)
    request.session.clear()
    return render(request,"firstpage.html")


def user_pannel(request):
    print(request)

   # customers=Room.objects.raw('select * from customer')
    users=User.objects.all
    total_count=User.objects.count()
    return render(request,"adminn/user_pannel.html",{'users': users,'total_count':total_count})

# update user
def update(request,p_id):
    #data verification
    users=User.objects.get(id=p_id)
    #bind data in form with instance of customer
    form =UserForm(request.POST, instance = users)
    if form.is_valid():
        try:
            form.save()
            return redirect("/user_pannel")
        except:
            print("validation false")
    return render(request,"adminn/user_edit.html",{'users':users})

# user_edit
def edit(request,p_id):
    users=User.objects.get(id=p_id)
    return render (request,"adminn/user_edit.html",{'users':users})


#user_delete
def delete(request,p_id):
    
    users=User.objects.get(id=p_id)
    users.delete()
    return redirect("/user_pannel")




#password




