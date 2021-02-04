
from django.urls import path
from . import views

# views is pointing to the browser returning the templates home.html
urlpatterns = [
    path('', views.home, name="home" ),
    path('about', views.about, name="about"),
    path('add_stock', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
]

