from django.db import models
import qrcode
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw
import re
import uuid

# URL Shortener
class URLShortener(models.Model):
    link = models.CharField(max_length=10000)
    alias = models.CharField(max_length=20, blank=True, null=True)
    uuid = models.CharField(max_length=20)

    
# QR Code Generator.
class QRCodeGenerator(models.Model):
    link = models.CharField(max_length=1000)
    alias = models.CharField(max_length=20, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return f"{str(self.link)}, {str(self.alias)}"

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.link)
        canvas = Image.new('RGB', (500, 500), 'white')
        qr_size = qrcode_img.size[0]
        qr_pos = (500 - qr_size) // 2
        canvas.paste(qrcode_img, (qr_pos, qr_pos))
        buffer = BytesIO()
        canvas.save(buffer, format='PNG')  # Save the canvas as the QR code image
        sanitized_link = re.sub(r'\W+', '_', self.link)  # Replace non-alphanumeric characters with underscores
        filename = f'qr_code-{self.alias or sanitized_link}.png'
        self.qr_code.save(filename, File(buffer), save=False)

        buffer.close()
        super().save(*args, **kwargs)


