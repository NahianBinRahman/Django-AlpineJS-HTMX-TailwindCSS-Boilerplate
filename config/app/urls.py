from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-content/', views.update_content, name='update_content'),
]
