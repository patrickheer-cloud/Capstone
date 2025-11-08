from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('Call', 'Call'),
        ('Email', 'Email'),
        ('Meeting', 'Meeting'),
    ]
    
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.activity_type} - {self.contact.name}"

class Task(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['due_date', '-created_at']
    
    def __str__(self):
        return f"{self.description[:50]} - {self.contact.name}"
    
    def is_due_today(self):
        return self.due_date == timezone.now().date()

class Sale(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='sales')
    item_description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()
    
    
    class Meta:
        ordering = ['-sale_date']
    
    def __str__(self):

        return f"${self.amount} - {self.contact.name}"
