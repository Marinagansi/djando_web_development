from django.shortcuts import render,redirect
from customer.forms import CustomerForm,CustomerUpdateForm
from customer.models import Customer
from django.contrib import messages


# Create your views here.
# registration customer
def customerform(request):
    print(request.FILES)
    if request.method=="POST":
        customers=CustomerForm(request.POST,request.FILES)
        # customers.save()
        result = customers.save()
        request.session['customer_id']=result.customer_id
        return redirect ("/home")
          

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
            # login(request, user)
                return redirect ("/home")
        except:
            print("invlalid")
            messages.info(request,"incorect username and password")

        return redirect ("/customer/signin")

    return render(request,'customer/clogin.html')

def customer_pannel(request):
    print(request)

   # customers=Room.objects.raw('select * from customer')
    customers=Customer.objects.all

    return render(request,"customer/customer_pannel.html",{'customers':customers})


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
            return redirect("/c_pannel")
        except:
            print("validation false")
    return render(request,"customer/c_edit.html",{'customers':customers})


def delete(request,p_id):
    
    customers=Customer.objects.get(customer_id=p_id)
    customers.delete()
    return redirect("/c_pannel")