from django.contrib import admin
from .models import Contact, Activity, Task, Sale

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email', 'phone']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['contact', 'activity_type', 'created_at']
    list_filter = ['activity_type', 'created_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['contact', 'description', 'due_date', 'completed']
    list_filter = ['completed', 'due_date']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['contact', 'item_description', 'amount', 'sale_date']
    list_filter = ['sale_date']