"""MJoyas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from portfolio.views import BrandView, HomeView, text_view

app_name = 'portfolio'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^products/', BrandView.as_view(), name = 'products'),
    url(r'^products/(?P<slug>[-\w]+)', text_view, name = 'text'),
    url(r'^us/', TemplateView.as_view(template_name = 'us.html'), name = 'us'),
    url(r'^contact/', TemplateView.as_view(template_name = 'contact.html'), name = 'contact'),
]