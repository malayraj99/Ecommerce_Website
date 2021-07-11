from django.db import models

import random
import os
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)

    new_filename = random.randint(1, 10000000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductManager(models.Manager):

    # def get_queryset(self):
    #     return self.get_queryset().filter(featured=featured)

    def get_by_id(self, id):
        # Product.objects == self.get_queryset()
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    # slug = models.SlugField(default='abc', blank=True)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def get_absolute_url(self):
        return("/products/{pk}/".format(pk=self.pk))

    def get_img(self):
        return self.image.url

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
