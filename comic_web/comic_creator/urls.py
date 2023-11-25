from django.urls import path
from .views import comic_create, generate_image, save_and_share, read_comic, edit_comic
from django.shortcuts import redirect

urlpatterns = [
    path('comic/read/<uuid:read_url>/', read_comic, name='read_comic'),
    path('comic/edit/<uuid:write_url>/', edit_comic, name='edit_comic'),
    path('comic/',comic_create,name='comic_create'),
    path('api/generate-image/', generate_image, name='generate_image'),
    path('save_and_share/', save_and_share, name='save_and_share'),
    path('', lambda request: redirect('comic_create')),
]
