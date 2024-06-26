from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form_view'),  # Set form_view as the default view
    path('dishes/<str:dish>', views.menuitem, name='menuitem'),
    path('home/', views.home),
    path('about/', views.about),
    path('say_hello/', views.say_hello),
    path('homepage/', views.homepage),
    path('display_date/', views.display_date),
    path('menu/', views.menu),
]