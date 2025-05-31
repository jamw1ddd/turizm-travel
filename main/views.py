from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')

def packages_view(request):
    return render(request, 'packages.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def booking_view(request):
    return render(request, 'booking.html')
