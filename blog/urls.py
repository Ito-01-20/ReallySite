from mysite import views
from django.urls import path, include
from blog import views

urlpatterns = [
    path('test/', views.test),
]