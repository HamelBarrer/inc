import uuid

from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from PIL import Image


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug


@receiver(pre_save, sender=Product)
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )
        instance.slug = slug


@receiver(pre_save, sender=Product)
def set_title(sender, instance, **kwargs):
    if instance.title:
        instance.title = instance.title.capitalize()


@receiver(post_save, sender=Product)
def set_image(sender, instance, *args, **kwargs):
    if instance.image:
        img = Image.open(instance.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(instance.image.path)
