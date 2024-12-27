from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    
    STATUS_CHOICES = (
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(null=True)

    def is_in_stock(self):
        if self.stock is None:
            return False
        return self.stock > 0
    is_in_stock.boolean = True

    def __str__(self):
        return self.name


class ProductReview(models.Model):

    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.user.username}"

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images', default='default_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.user.username} - {self.product.name}"