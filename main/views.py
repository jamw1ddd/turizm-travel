from django.shortcuts import render
from .models import Package, GalleryItem, Booking
from .forms import BookingForm, SubscriberForm, ContactForm
from django.shortcuts import redirect

# Create your views here.
def home_view(request):
    package = Package.objects.all()
    item = GalleryItem.objects.all()
    booking = Booking.objects.all()
    categories = [
        {'key': 'all', 'label': 'Hammasi'},
        {'key': 'historical', 'label': 'Tarixiy joylar'},
        {'key': 'nature','label': 'Tabiat go‘zalliklari'},
        {'key': 'mountain','label': 'Tog‘ sayohatlari'},
        {'key': 'desert','label': 'Cho‘l safari'},
    ]
    context = {
        'packages': package,
        'categories': categories,
        'items': item,
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def packages_view(request):
    package = Package.objects.all()
    return render(request, 'packages.html', {'packages': package})

def gallery_view(request):
    items = GalleryItem.objects.all()

    # Kategoriya kalitlari — templatda navigatsiya uchun ishlatiladi
    categories = [
        {'key': 'all', 'label': 'Hammasi'},
        {'key': 'historical', 'label': 'Tarixiy joylar'},
        {'key': 'nature','label': 'Tabiat go‘zalliklari'},
        {'key': 'mountain','label': 'Tog‘ sayohatlari'},
        {'key': 'desert','label': 'Cho‘l safari'},
    ]

    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'gallery.html', context)

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')  # Sahifangizda bu URL mavjud bo‘lishi kerak
    else:
        form = BookingForm()

    packages = Package.objects.all()
    return render(request, 'booking.html', {'form': form, 'packages': packages})


def subscribe_view(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')  # Xabar muvaffaqiyatli yuborildi sahifasi
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
