from django.contrib import admin
from .models import QRCodeGenerator, URLShortener

# Register your models here.
admin.site.register(QRCodeGenerator)
admin.site.register(URLShortener)

