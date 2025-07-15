from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('buyer/add/', views.CreateBuyer.as_view(), name='add_buyer'),
    path('buyer/<int:pk>/', views.UpdateBuyer.as_view(), name='update_buyer'),
    path('buyer/list/', views.ListBuyers.as_view(), name='list_buyers'),
    path('buyer/<int:pk>/delete/', views.DeleteBuyer.as_view(), name='delete_buyer'),
]
