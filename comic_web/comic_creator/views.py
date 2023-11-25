from django.shortcuts import render
from django.http import JsonResponse
import requests
import io
import base64
from PIL import Image
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env')
load_dotenv(dotenv_path)
API_URL = os.getenv('API_URL')
HEADERS = eval(os.getenv('HEADERS'))

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Comic, Panel, ImageElement, TextElement
from django.shortcuts import render, get_object_or_404

def create_comic_model():
    # Create a new Comic model instance
    comic = Comic.objects.create()

    # Generate panels for the comic
    panels = []
    for i in range(1, 11):
        image_element = ImageElement.objects.create()
        text_element = TextElement.objects.create()
        panel = Panel.objects.create(image_element=image_element, text_element=text_element)
        panels.append(panel)
        
    comic.panels.set(panels)

    # Generate read and write URLs
    read_url = comic.read_url
    write_url = comic.write_url

    return comic, read_url, write_url

@csrf_exempt
@require_POST
def save_and_share(request):
    try:
        data = json.loads(request.body.decode('utf-8'))['data']
        checker_url = json.loads(request.body.decode('utf-8'))['checker_url']
        if not data:
            return JsonResponse({'success': False, 'error': 'No data received.'}, status=400)

        # Create a new comic model
        if 'edit' in checker_url:
            w = checker_url.find('edit')
            comic = get_object_or_404(Comic, write_url=checker_url[w+5:-1])
            read_url = comic.read_url
            write_url = comic.write_url
        else:
            comic, read_url, write_url = create_comic_model()
            
        # Update the comic model with the received data
        for index, panel_data in enumerate(data):
            try:
                panel = comic.panels.all()[index]
                panel.image_element.image_url = panel_data['image_url']
                panel.text_element.content = panel_data['text_content']
                panel.image_element.save()
                panel.text_element.save()
            except Panel.DoesNotExist:
                return JsonResponse({'success': False, 'error': f'Panel {index} does not exist.'}, status=404)

        # Save the changes to the comic model
        comic.save()

        return JsonResponse({'success': True, 'read_url': str(read_url), 'write_url': str(write_url)})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def read_comic(request, read_url):
    comic = get_object_or_404(Comic, read_url=read_url)
    return render(request, 'read_comic.html', {'comic': comic})

def edit_comic(request, write_url):
    comic = get_object_or_404(Comic, write_url=write_url)
    return render(request, 'write_comic.html', {'comic':comic})
    
def generate_image(request):
    panel_text = request.GET.get('text', '')
    
    image_bytes = query_hugging_face_api({"inputs": panel_text})
    image = Image.open(io.BytesIO(image_bytes))

    # Convert the Image object to bytes
    image_bytes_io = io.BytesIO()
    image.save(image_bytes_io, format='PNG')
    image_base64 = base64.b64encode(image_bytes_io.getvalue()).decode('utf-8')

    # Return the image in the API response
    return JsonResponse({'image': image_base64})

def query_hugging_face_api(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.content

def comic_create(request):
    return render(request,'home.html')