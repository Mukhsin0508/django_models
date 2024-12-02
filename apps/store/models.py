from django.db import models

class Store(models.Model):
    # Basic Store Info
    name = models.CharField(max_length=255)
    store_id = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    # Store Operations
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_open_24_hours = models.BooleanField(default=False)
    total_employees = models.IntegerField()
    manager_name = models.CharField(max_length=255)
    established_date = models.DateField()
    # Financials and Metrics
    monthly_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    average_transaction_value = models.DecimalField(max_digits=8, decimal_places=2)
    total_inventory_value = models.DecimalField(max_digits=12, decimal_places=2)
    # Store Preferences and Settings
    accepts_online_orders = models.BooleanField(default=True)
    is_franchise = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=True)
    supports_contactless_payment = models.BooleanField(default=True)
    customer_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    # Additional Info
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)

def __str__(self):
    return f"{self.store_name} - {self.city}"

class Meta:
    verbose_name = 'Store'
    verbose_name_plural = 'Stores'
    ordering = ['-created_at']