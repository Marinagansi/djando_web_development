from django.shortcuts import render,redirect
from contact.forms import ContactForm

# Create your views here.
def contactpage(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        form.save()
        return redirect ('/home')
              
    else:
        form=ContactForm()
    return render (request,"contact.html",{'form':form})