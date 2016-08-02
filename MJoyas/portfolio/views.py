from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

class BrandView(ListView):	
	template_name = 'products.html'
	queryset = models.Brand.objects.order_by('brand_name')
	context_object_name = 'brand_list'

class TextView(DetailView):
	template_name = 'brands/brand_text.html'	
	context_object_name = 'brand'
	model = models.Brand

class HomeView(ListView):
	template_name = 'home.html'
	queryset = models.HomeHeader.objects.all()