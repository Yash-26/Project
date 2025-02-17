from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('identify/', views.identify, name='identify'),
   
    path('emotions/', views.emotions, name='emotions'),
    path('emotion_data_view/', views.emotion_data_view, name='emotion_data_view'),
    
    path('home/', views.landingpage, name='landingpage'),

    path('register/', views.register, name='register'),

    path('',views.login, name='login'),
   
    
]