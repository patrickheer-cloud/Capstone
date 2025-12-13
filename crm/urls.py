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
