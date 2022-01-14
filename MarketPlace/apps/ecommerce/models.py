from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
  name = models.CharField(max_length=256, unique=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
  slug = models.SlugField(max_length=256, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  
  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    value = self.name
    if not self.slug:
      self.slug = slugify(value, allow_unicode=True)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('items-by-category', args=[str(self.slug)])

class Item(models.Model):
    title = models.CharField(max_length=256)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(
      max_length=256
    )

    def __str__(self):
      return self.title

    def get_absolute_url(self):
      kwargs = {
        'slug': self.slug
      }
      return reverse('item-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
      if not self.slug:
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
      super().save(*args, **kwargs)
