from django.db import models
from users.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name


class Product(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )

    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, default='U', choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_kids = models.BooleanField(default=False)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    short_description = models.CharField(max_length=30, null=True, blank=True, default='Shoes')
    special_prod = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    def pre_save(self):
        if self.price and self.price != self.old_price:
            self.old_price = self.price

    def count_discount(self):
        if self.price is not None and self.old_price is not None and self.price < self.old_price:
            return round(((self.old_price - self.price) / self.old_price) * 100)
        else:
            return 0


class SliderImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product.name + ' Image'


class ProdImage(models.Model):
    image = models.ImageField(upload_to='product_images/', default='default_image.jpg')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True)

    def __str__(self):
        return self.image.name + ' Image'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Basket for {self.user.first_name} | Product: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity