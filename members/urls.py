from django.urls import path
from . import views
from .views import finance_data_view

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('fdr/', views.finance_data_view, name='finance_data'),
    path('fdr_show_image', views.finance_data_view_show_image, name='finance_data_view_show_image'),
]