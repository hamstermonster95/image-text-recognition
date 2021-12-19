from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from imagetext.settings import MEDIA_ROOT
import pytesseract
from PIL import Image




def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        #pytesseract.pytesseract.tesseract_cmd=r'/opt/homebrew/Cellar/tesseract/4.1.3/bin/tesseract'
        text=pytesseract.image_to_string(Image.open(MEDIA_ROOT+'/'+myfile.name))
        
        text = text.encode("ascii", "ignore")
        text = text.decode()
                

                # Summary (0.1% of the original content).

        return render(request, 'simple_upload.html', { 'text' :
             text
        })
    return render(request, 'simple_upload.html')
