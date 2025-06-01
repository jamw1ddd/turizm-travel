from django.contrib import admin
from .models import Package, GalleryItem, Booking, Subscriber, ContactMessage

admin.site.register(Package)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)

admin.site.register(Booking)
admin.site.register(Subscriber)
admin.site.register(ContactMessage)