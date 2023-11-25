from django.contrib import admin
from .models import Comic, ImageElement, TextElement, Panel

# Register your models here.
admin.site.register(ImageElement)
admin.site.register(TextElement)
admin.site.register(Panel)
admin.site.register(Comic)

