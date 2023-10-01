from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Listing, Band

def band_list(request):
    return render(request,'listing/band_list.html', {'bands' : Band.objects.all()})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,'listing/band_detail.html',{'band': band})

def about(request):
    return render(request, 'listing/about.html')

def contactus(request):
    return render(request, 'listing/contact.html')

def listing(request):
    return render(request, 'listing/listing.html',{'listings' : Listing.objects.all()})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,'listing/listing_detail.html',{'listing': listing})

