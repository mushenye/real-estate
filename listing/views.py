from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm
# Create your views here.

def home (request):
     return HttpResponse("hello world")
 
def listing_list(request):
    listings= Listing.objects.all()
    context= {
        'listings':listings
    }
    return render(request,'listing/listing.html', context)


def listing_retrieve(request, pk):
    listing =Listing.objects.get(id=pk)
    context= {
        'listing':listing
    }
    return render(request,'listing/listing_retrieve.html', context)



def listing_create(request):
    form = ListingForm()
    if request.method=="POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/listing/')
    context= {
        'form':form
    }
    return render(request,'listing/listing_create.html', context)

def listing_update(request, pk):
    listing= Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method=="POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save() 
            return redirect('/listing/')
    context= {
        'form':form
    }
    return render(request,'listing/listing_update.html', context)


def listing_delete(request, pk):
    listing= Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/listing/')