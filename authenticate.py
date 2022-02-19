from django.contrib import messages
from django.shortcuts import redirect
from customer.models import Customer

class Authentication:
    def valid_user(function):
        def wrap(request):
            print(request)  
            try:
                Customer.objects.get(customer_name=request.session['customer_name'],customer_password=request.session['customer_password'])
                return function (request)
            except:
                print('no authentication')
                messages.warning(request,'enter valid user')
            return redirect('/customer/signin')
        return wrap

    def valid_user_where_id(function):
        def wrap(request,p_id):
            try:
                Customer.objects.get(customer_name=request.session['customer_name'],customer_password=request.session['customer_password'])
                return function(request)
            except:
                print('no authentication')
                messages.warning(request,'enter valid user')
            return redirect('/home')
        return wrap

