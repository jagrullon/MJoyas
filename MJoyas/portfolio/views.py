from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models

class BrandView(ListView):	
	template_name = 'products.html'
	queryset = models.Brand.objects.order_by('brand_name')
	context_object_name = 'brand_list'

def text_view(request, slug):
	brand = models.Brand.objects.get(slug = slug)
	brand_text = models.BrandText.objects.get(brand = brand)
	return render(request, 'brands/brand_text.html', {'brand_text': brand_text,})	

class HomeView(ListView):
	template_name = 'home.html'
	queryset = models.HomeHeader.objects.all()