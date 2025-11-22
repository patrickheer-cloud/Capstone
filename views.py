from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from datetime import datetime, date
from .models import Contact, Activity, Task, Sale

def contact_list(request):
    contacts = Contact.objects.all()
    
    # Check for tasks due today
    today = date.today()
    due_tasks = Task.objects.filter(due_date=today, completed=False)
    
    context = {
        'contacts': contacts,
        'due_tasks': due_tasks,
    }
    return render(request, 'crm/contact_list.html', context)

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    activities = contact.activities.all()
    tasks = contact.tasks.filter(completed=False)
    sales = contact.sales.all()[:5]  # Show last 5 sales
    
    context = {
        'contact': contact,
        'activities': activities,
        'tasks': tasks,
        'sales': sales,
    }
    return render(request, 'crm/contact_detail.html', context)

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        messages.success(request, 'Contact added successfully!')
        return redirect('contact_list')
    
    return render(request, 'crm/add_contact.html')

def log_activity(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    
    if request.method == 'POST':
        activity_type = request.POST.get('activity_type')
        summary = request.POST.get('summary')
        
        Activity.objects.create(
            contact=contact,
            activity_type=activity_type,
            summary=summary
        )
        messages.success(request, 'Activity logged successfully!')
        return redirect('contact_detail', pk=contact_pk)
    
    return render(request, 'crm/log_activity.html', {'contact': contact})

def add_task(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    
    if request.method == 'POST':
        description = request.POST.get('description')
        due_date_str = request.POST.get('due_date')
        
        try:
            due_date = datetime.strptime(due_date_str, '%m/%d/%Y').date()
            Task.objects.create(
                contact=contact,
                description=description,
                due_date=due_date
            )
            messages.success(request, 'Task added successfully!')
            return redirect('contact_detail', pk=contact_pk)
        except ValueError:
            messages.error(request, 'Invalid date format. Please use MM/DD/YYYY')
    
    return render(request, 'crm/add_task.html', {'contact': contact})

def complete_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.completed = True
    task.save()
    messages.success(request, 'Task marked as complete!')
    return redirect('contact_detail', pk=task.contact.pk)

def log_sale(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    
    if request.method == 'POST':
        item_description = request.POST.get('item_description')
        amount = request.POST.get('amount')
        sale_date_str = request.POST.get('sale_date')
        
        try:
            sale_date = datetime.strptime(sale_date_str, '%m/%d/%Y').date()
            Sale.objects.create(
                contact=contact,
                item_description=item_description,
                amount=amount,
                sale_date=sale_date
            )
            messages.success(request, 'Sale logged successfully!')
            return redirect('contact_detail', pk=contact_pk)
        except ValueError:
            messages.error(request, 'Invalid date format. Please use MM/DD/YYYY')
    
    return render(request, 'crm/log_sale.html', {'contact': contact})

def sales_list(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    sales = contact.sales.all()
    total = sales.aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'contact': contact,
        'sales': sales,
        'total': total,
    }
    return render(request, 'crm/sales_list.html', context)

def sales_history(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    
    # Aggregate sales by month
    monthly_sales = (
        contact.sales
        .annotate(month=TruncMonth('sale_date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )
    
    # Prepare data for chart
    months = [sale['month'].strftime('%b %Y') for sale in monthly_sales]
    amounts = [float(sale['total']) for sale in monthly_sales]
    
    context = {
        'contact': contact,
        'months': months,
        'amounts': amounts,
    }
    return render(request, 'crm/sales_history.html', context)

# ============================================================================
# FILE: crm/urls.py
# ============================================================================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/add/', views.add_contact, name='add_contact'),
    path('contact/<int:contact_pk>/log-activity/', views.log_activity, name='log_activity'),
    path('contact/<int:contact_pk>/add-task/', views.add_task, name='add_task'),
    path('task/<int:task_pk>/complete/', views.complete_task, name='complete_task'),
    path('contact/<int:contact_pk>/log-sale/', views.log_sale, name='log_sale'),
    path('contact/<int:contact_pk>/sales-list/', views.sales_list, name='sales_list'),
    path('contact/<int:contact_pk>/sales-history/', views.sales_history, name='sales_history'),
]