from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def nav(request):
    return render(request,"nav.html")

def firstpage(request):
    return render(request,"firstpage.html")




# @login_required(login_url='/customer/signin')
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
            return redirect ("/cloth_pannel")

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
    
    
    return render(request,"registration.html")

def logout_page(request):
    logout(request)
    request.session.clear()
    return render(request,"firstpage.html")


def user_pannel(request):
    print(request)

   # customers=Room.objects.raw('select * from customer')
    users=User.objects.all

    return render(request,"adminn/user_pannel.html",{'users': users})

# update user
def update(request,p_id):
    #data verification
    users=User.objects.get(id=p_id)
    #bind data in form with instance of customer
    form =User(request.POST, instance = request.user)
    if form.is_valid():
        try:
            form.save()
            return redirect("/c_pannel")
        except:
            print("validation false")
    return render(request,"adminn/user_edit.html",{'users':users})


def edit(request,p_id):
    users=User.objects.get(id=p_id)
    return render (request,"adminn/user_edit.html",{'users':users})

