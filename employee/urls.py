from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.employees_list, name='employees-list'),
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit-employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete-employee'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)