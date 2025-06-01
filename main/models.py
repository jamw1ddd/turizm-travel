from django.db import models
from django.utils import timezone


class Package(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    persons = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='packages/')
    rating = models.PositiveSmallIntegerField(default=5)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('all', 'Hammasi'),
        ('historical', 'Tarixiy joylar'),
        ('nature', 'Tabiat go‘zalliklari'),
        ('mountain', 'Tog‘ sayohatlari'),
        ('desert', 'Cho‘l safari'),
    ]

    image = models.ImageField(upload_to='gallery/')            # Galereya rasmi
    category = models.CharField(max_length=20, 
                                choices=CATEGORY_CHOICES, 
                                default='all')                  # Rasm kategoriya turi
    title = models.CharField(max_length=100, default='Sayohat') # Rasmlar sarlavhasi
    lightbox_group = models.CharField(
        max_length=50, 
        default='gallery'
    )

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"
    

class Booking(models.Model):
    CATEGORY_CHOICES = [
        ('family', 'Oila'),
        ('individual', 'Yakka'),
        ('group', 'Guruh'),
        ('kids', 'Bolalar'),
    ]

    name = models.CharField("Ism", max_length=100)
    phone = models.CharField("Telefon raqam", max_length=20)
    date_time = models.DateTimeField("Sana va vaqt")
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, verbose_name="Sayohat yo'nalishi")
    persons = models.PositiveIntegerField("Nechta kishi")
    category = models.CharField("Toifa", max_length=20, choices=CATEGORY_CHOICES)
    message = models.TextField("Maxsus iltimos", blank=True)
    created_at = models.DateTimeField("Yaratilgan vaqt", default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.package}"
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class ContactMessage(models.Model):
    ism = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Elektron pochta")
    mavzu = models.CharField(max_length=200, verbose_name="Mavzu")
    xabar = models.TextField(verbose_name="Xabar")
    sana = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan sana")

    def __str__(self):
        return f"{self.ism} - {self.mavzu}"

    class Meta:
        verbose_name = "Kontakt xabar"
        verbose_name_plural = "Kontakt xabarlari"
