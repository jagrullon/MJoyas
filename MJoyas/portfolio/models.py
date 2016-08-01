from django.db import models

class HomeHeader(models.Model):
	title = models.CharField(max_length = 155)
	header = models.TextField()

	def __unicode__(self):
		return self.header		

class Brand(models.Model):
	brand_name = models.CharField(max_length = 155)
	slug = models.SlugField(unique = True)

	def __unicode__(self):
		return self.brand_name

class BrandText(models.Model):
	brand = models.OneToOneField(Brand, on_delete = models.CASCADE, primary_key = True)
	description = models.TextField()

	def __unicode__(self):
		return self.description
		