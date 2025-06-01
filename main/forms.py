from django import forms
from .models import Booking,Subscriber, ContactMessage

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'date_time', 'package', 'persons', 'category', 'message']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['ism', 'email', 'mavzu', 'xabar']
        labels = {
            'ism': 'Ismingiz',
            'email': 'Elektron pochta',
            'mavzu': 'Mavzu',
            'xabar': 'Xabar',
        }
        widgets = {
            'ism': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Elektron pochta'}),
            'mavzu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mavzu'}),
            'xabar': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabar', 'rows': 6}),
        }