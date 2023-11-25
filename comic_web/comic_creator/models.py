# models.py
from django.db import models
import uuid

class TextElement(models.Model):
    content = models.TextField()

    def __str__(self):
        return f'TextElement {self.pk}'

class ImageElement(models.Model):
    image_url = models.URLField()

    def __str__(self):
        return f'ImageElement {self.pk}'

class Panel(models.Model):
    image_element = models.ForeignKey(ImageElement, on_delete=models.CASCADE)
    text_element = models.ForeignKey(TextElement, on_delete=models.CASCADE)

    def __str__(self):
        return f'Panel {self.pk}'

class Comic(models.Model):
    panels = models.ManyToManyField(Panel, related_name='comic_panels')
    read_url = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    write_url = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'Comic {self.pk}'
