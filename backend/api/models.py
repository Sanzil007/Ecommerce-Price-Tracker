from django.db import models

class Product(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    current_price = models.FloatField(default=0.0)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or self.url

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, related_name='price_history', on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.title} - ${self.price} on {self.date}"
