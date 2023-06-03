from django.shortcuts import render, redirect
from .models import QRCodeGenerator, URLShortener
from django.http import HttpResponse
import uuid

# URL Link Shortener
def create(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        alias = request.POST.get('alias')
        uid =  str(uuid.uuid4())[:5]
        
        new_url = URLShortener(link=link, alias=alias, uuid=uid)
        new_url.save()

        if alias:
            return HttpResponse(alias)
        else:
            return HttpResponse(uid)

# Create your views here.
def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        alias = request.POST.get('alias')
        qr_obj = QRCodeGenerator.objects.create(link=link, alias=alias)
        request.session['qr_code_id'] = qr_obj.id  # Store the QR code ID in the session
        return redirect('index')
    
    page_title = 'Home Page'
    qr_code_id = request.session.pop('qr_code_id', None)  # Retrieve and remove the QR code ID from the session
    if qr_code_id:
        qr_obj = QRCodeGenerator.objects.filter(id=qr_code_id).last()  # Get the QR code object with the stored ID
        qr_objs = [qr_obj] if qr_obj else []  # Wrap the single object in a list
        qr_obj.delete()  # Delete the QR code object
    else:
        qr_objs = []  # No QR code object available if ID is not found
    
    context = {
        'page_title': page_title,
        'qr_obj': qr_objs,
    }
    return render(request, 'index.html', context)


