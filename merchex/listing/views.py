from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listing.models import Listing, Band
from listing.forms import BandForm, ContactUsForm, ListingForm

def band_list(request):
    return render(request,'listing/band_list.html', {'bands' : Band.objects.all()})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,'listing/band_detail.html',{'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else: # GET
        form = BandForm()

    return render(request,'listing/band_create.html', {'form': form})

def about(request):
    return render(request, 'listing/about.html')

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email-sent', email = form.cleaned_data['email'])
    else:
        form = ContactUsForm()

    return render(request, 'listing/contact.html', {'form' : form})

def email_sent(request, email):
    return render(request, 'listing/email_sent.html', {'email' : email})

def listing(request):
    return render(request, 'listing/listing.html',{'listings' : Listing.objects.all()})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,'listing/listing_detail.html',{'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else: # GET
        form = ListingForm()

    return render(request,'listing/listing_create.html', {'form': form})

