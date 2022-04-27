from django.db import models
import uuid

# Create your models here.


class Flan (models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    price = models.IntegerField(null=True, blank=True, default=None)


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


class Local (models.Model):
    id = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=64)
    direccion = models.TextField()
    telefono = models.CharField(max_length=64)
    image_url = models.URLField()
    
