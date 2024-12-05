"""
URL configuration for contactlist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('success', views.success, name='success'),
    path('contact/<int:pk>', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/delete', views.contact_delete, name='contact_delete'),
    path('contact/create', views.contact_create, name='contact_create'),
    path('recommend_contacts', views.recommend_contacts, name="recommend_contacts"),
    # path('save_contact', views.save_contact, name="save_contact"),
]
