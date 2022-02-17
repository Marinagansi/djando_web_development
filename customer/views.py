from django.shortcuts import render,redirect
from customer.forms import CustomerForm,CustomerUpdateForm
from customer.models import Customer
from django.contrib import messages
from booking.models import Booking
from store.models import Cloths
from django.core.mail import send_mail
from authenticate import Authentication


 
# Create your views here.
# registration customer
def customerform(request):
    print(request.FILES)
    if request.method=="POST":
        customers=CustomerForm(request.POST,request.FILES)
        if customers.is_valid():
            try:
        # customers.save()
                result = customers.save()
                f_name = request.POST['customer_name']
                f_email = request.POST['customer_email']

                send_mail(
                    f_name, #subject
                    'Welcome to stylelook you have been register' , #message'h
                    f_email, #from email
                    ['gansimarina@gmail.com'], # To Email

                 )
                request.session['customer_id']=result.customer_id
                return redirect ("/home")
            except:
                print("INVALID")
        
          

    else:
        customers=CustomerForm()
     
    return render (request,"customer/Cregistration.html",{'customers':customers})

#login customer
def signin(request):
    print(request)
    if request.method=='POST':
        customer_name=request.POST.get("customer_name")
        customer_password=request.POST.get("customer_password")
        try:

            user=Customer.objects.get(customer_name=customer_name,customer_password=customer_password)

        # user = authenticate(request, username=customer_name,password=customer_pasword)
        # print(user)
            if user is not None:
            
                request.session['customer_id']=user.customer_id
                request.session['customer_name']=user.customer_name
                request.session['customer_password']=user.customer_password
            # login(request, user)
                return redirect ("/home")
        except:
            print("invlalid")
            messages.info(request,"incorect username and password")

        return redirect ("/customer/signin")

    return render(request,'customer/clogin.html')

def customer_pannel(request):
    print(request)
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*3
        print(offset)
    else:
        offset=0
        page=1

   # customers=Room.objects.raw('select * from customer')
    # customers=Customer.objects.all
    customers=Customer.objects.raw("select * from customer limit 3 offset % s",[offset])
    pageItem=len(customers)
    booking_count=Booking.objects.count()
    total_count=Customer.objects.count()
    cloths_count=Cloths.objects.count()
    return render(request,"customer/customer_pannel.html",{'customers':customers,'page':page,'pageItem':pageItem,'total_count':total_count,'booking_count':booking_count,'cloths_count':cloths_count})


    # return render(request,"customer/customer_pannel.html",{'customers':customers})


def edit(request,p_id):
    customers=Customer.objects.get(customer_id=p_id)
    return render (request,"customer/c_edit.html",{'customers':customers})
  


def update(request,p_id):
    #data verification
    customers=Customer.objects.get(customer_id=p_id)
    #bind data in form with instance of customer
    form =CustomerUpdateForm(request.POST, instance=customers)
    if form.is_valid():
        try:
            form.save()
            return redirect("/customer/c_pannel")
        except:
            print("validation false")
    return render(request,"customer/c_edit.html",{'customers':customers})


def delete(request,p_id):
    
    customers=Customer.objects.get(customer_id=p_id)
    customers.delete()
    return redirect("/customer/c_pannel")


def logout_customer(request):
    request.session.clear()
    return render (request,"firstpage.html")


def editp(request,name):
    customers=Customer.objects.get(customer_name=name)
    return render (request,"customer/clogin.html",{'customers':customers})

def forget(request,name):
    customers=Customer.objects.get(customer_name=name)
    #bind data in form with instance of customer
    form =CustomerUpdateForm(request.POST, instance=customers)
    if form.is_valid():
        try:
            form.save()
            return redirect("/c_pannel")
        except:
            print("validation false")
    return render (request,"customer/forget_password.html",{'customers':customers})
