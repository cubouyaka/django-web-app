"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listing import views

urlpatterns = [
path('admin/', admin.site.urls),
path('bands/', views.band_list, name='band-list'),
path('bands/<int:id>/', views.band_detail, name='band-detail'),
path('bands/add/', views.band_create, name='band-create'),
path('about/', views.about),
path('contactus/', views.contactus, name='contactus'),
path('email_sent/<email>', views.email_sent, name='email-sent'),
path('listing/', views.listing, name='listing-list'),
path('listing/<int:id>/', views.listing_detail, name='listing-detail'),
path('listing/add/', views.listing_create, name='listing-create'),
]
