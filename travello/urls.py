from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('contact_list',views.contact_list, name='contact_list'),  
    path('contact_edit/<int:id>', views.contact_edit, name='contact_edit'),  
    path('contact_update/<int:id>', views.contact_update, name='contact_update'),  
    path('contact_destroy/<int:id>', views.contact_destroy, name='contact_destroy') 
]