from django.urls import path
from .views import home_view,about_view,contact_view, services_view, packages_view, gallery_view,booking_view, subscribe_view


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('services/', services_view, name='services'),
    path('packages/', packages_view, name='packages'),
    path('gallery/', gallery_view, name='gallery'),
    path('booking/', booking_view, name='booking'),
    path('subscribe/', subscribe_view, name='subscribe'),
]
