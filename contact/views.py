from django.shortcuts import render,redirect
from contact.forms import ContactForm
from contact.models import Contact

# Create your views here.
def contactpage(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        form.save()
        return redirect ('/home')
              
    else:
        form=ContactForm()
    return render (request,"contact/contact.html",{'form':form})

def message(request):
    print(request)
    if(request.method=="POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if ('next' in request.POST):
             page=page+1
        tempOffSet = page - 1
        offset=tempOffSet*4
        print(offset)
    else:
        offset=0
        page=1

   # customers=Room.objects.raw('select * from customer')
    # customers=Customer.objects.all
    contacts=Contact.objects.raw("select * from contact limit 4 offset % s",[offset])
    pageItem=len(contacts)
    return render(request,"contact/message_pannel.html",{'contacts':contacts,'page':page,'pageItem':pageItem})
