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
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_kids = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SliderImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product.name + ' Image'