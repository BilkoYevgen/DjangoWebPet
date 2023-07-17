from django.db import models

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
    image = models.ImageField(upload_to='product_images/', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_kids = models.BooleanField(default=False)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    short_description = models.CharField(max_length=30, null=True, blank=True, default='Shoes')

    def __str__(self):
        return self.name

    def pre_save(self):
        if self.price and self.price != self.old_price:
            self.old_price = self.price

    def count_discount(self):
        if self.price < self.old_price:
            return round(((self.old_price - self.price) / self.old_price) * 100)
        else:
            return 0


class SliderImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product.name + ' Image'