from django.contrib import admin
from django.urls import path

from .views import home_page_views

urlpatterns = [
    path("", home_page_views),
    path('admin/', admin.site.urls),
]
