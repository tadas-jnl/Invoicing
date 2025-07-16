from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('buyer/<int:pk>/', views.UpdateBuyer.as_view(), name='update_buyer'),
    path('buyer/list/', views.ListBuyers.as_view(), name='list_buyers'),
    path('buyer/add/', views.CreateBuyer.as_view(), name='add_buyer'),
    path('buyer/<int:pk>/delete/', views.DeleteBuyer.as_view(), name='delete_buyer'),
    path('invoice/list/', views.ListInvoices.as_view(), name="list_invoices"),
    path('invoice/<int:pk>/', views.DetailInvoice.as_view(), name='detail_invoice'),
    path('invoice/create/', views.CreateInvoice.as_view(), name='create_invoice'),
    path('invoice/<int:pk>/update/', views.UpdateInvoice.as_view(), name='update_invoice'),
    path('invoice/<int:pk>/delete/', views.DeleteInvoice.as_view(), name='delete_invoice'),
    path('invoice/<int:pk>/createitem/', views.CreateInvoiceItem.as_view(), name='create_item'),
    path('invoice/item/<int:pk>/update/', views.UpdateInvoiceItem.as_view(), name='update_item'),
    path('invoice/item/<int:pk>/delete/', views.DeleteInvoiceItem.as_view(), name='delete_item'),
]
