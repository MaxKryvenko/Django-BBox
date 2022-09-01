from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.



class NativeInOut(models.Model):
	video_choices = (("VGA","VGA"), 
	 					("DVI","DVI"),
						("HDMI","HDMI"),
	 					("DP", "DsiplayPort"),)
	native_inout = models.CharField(max_length=10, choices=video_choices)#, blank=True, null=True)

	def __str__(self):
		return self.native_inout


class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(max_digits=100, decimal_places=2)
	summary 	= models.TextField(default='default summary')
	resolution_choices = (("4K","4K60"), 
						("HD","Full HD"),)
	max_resolution  = models.CharField(max_length=10, choices=resolution_choices,blank=True, null=True)
	main_image	= models.ImageField(upload_to='static/images/', blank=True, null=True)
	native_in_out_choices = {"VGA":"VGA","DVI":"DVI", "HDMI":"HDMI","DP": "DsiplayPort"}
	native_in_out = models.ManyToManyField(NativeInOut, blank=True)#, limit_choices_to=native_in_out_choices,blank=True, null=True)
	speed_choices = (('1Gbe', '1G'), ('10Gbe', '10G'))
	speed = MultiSelectField(choices=speed_choices, blank=True, null=True)


	def get_absolute_url(self):
		return reverse("products:product_detail", kwargs={"id": self.id})
		# return f"/product/{self.id}"

	def __str__(self):
		return self.title

