from django.db import models
 
class HomeHeader(models.Model):
	title = models.CharField(max_length = 155)
	header = models.TextField()

	def __unicode__(self):
		return self.header		

class Brand(models.Model):
	brand_name = models.CharField(max_length = 155)
	description = models.TextField(default = '')	
	slug = models.SlugField(unique = True)

	def __unicode__(self):
		return self.brand_name
		