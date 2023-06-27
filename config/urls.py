from django.contrib import admin
from django.urls import path

from nasa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.get_home_page, name='home'),
]

