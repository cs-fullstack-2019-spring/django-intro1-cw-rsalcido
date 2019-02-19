from django.urls import path
from . import views

# specific paths with view names to call functions to perform actions on the views.py

urlpatterns = [

    path('music/', views.music, name="index"),
    path('John_Legend', views.John_Legend, name="index"),
    path('Brain_Mcknight', views.Brain_Mcknight, name="index"),
    path('Lil_Wayne', views.Lil_Wayne, name="index"),
]
