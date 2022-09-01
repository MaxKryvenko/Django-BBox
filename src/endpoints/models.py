from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import mark_safe






# Create your models here.
class SwitchingControl(models.Model):
	switching_control = models.CharField(max_length=30)
	def __str__(self):
		return self.switching_control

class NetworkMediaType(models.Model):
	media_type = models.CharField(max_length=20)	
	def __str__(self):
		return self.media_type

class AccessToVirtualResources(models.Model):
	access_to_virtual_sources = models.CharField(max_length=30)
	class Meta:
		verbose_name_plural='2. Access to Virtual Sources'
	def __str__(self):
		return self.access_to_virtual_sources

class AudioType(models.Model):
	audio_type = models.CharField(max_length=20)
	def __str__(self):
		return self.audio_type

def get_upload_to(instance, filename):
	return 'static/images/%s/%s' % (instance.sku, filename)


class Endpoint(models.Model):

	class Meta:
		verbose_name_plural='1. Endpoints'
# Main attributes
	sku 		= models.SlugField("SKU",max_length=20)
	solution 	= models.ForeignKey('solutions.Solution', on_delete=models.CASCADE)
	# created_by	= models.ForeignKey(User, on_delete=models.DO_NOTHING)

	status_choices = (('Available' , 'Available'), ('EOL', 'End of Life'))
	status 		= models.CharField(max_length=20,choices = status_choices,default='Available')
	description = models.TextField(blank=True, null=True, max_length=1000 ,default='Describe this Product here')
	summary 	= models.TextField(default='short summary', max_length=100)
	main_image	= models.ImageField(upload_to=get_upload_to , help_text='Upload a Photo with a General view')
	front_image	= models.ImageField(upload_to=get_upload_to, help_text='Upload a Photo with a Frontal view')
	back_image	= models.ImageField(upload_to=get_upload_to, help_text='Upload a Photo with a BackEnd view')


	
	endpoint_mode_choices = (('Transmitter' , 'Transmitter'), ('Receiver', 'Receiver'), ('Tranceiver' , 'Tranceiver'),)
	endpoint_mode = models.CharField(max_length=15, choices=endpoint_mode_choices)

	endpoint_type_choices = (('Hardware' , 'Hardware'), ('Software', 'Software'))
	endpoint_type = models.CharField(max_length=10, choices=endpoint_type_choices, default='Hardware')

	switching_control = models.ManyToManyField(SwitchingControl, help_text='Select ALL that apply')

# Video attributes
	head_choices = (("Single","Single"), ("Dual","Dual"),)
	head_count = models.CharField(max_length=10, choices=head_choices, default='Single')

	resolution_choices = (("1080p30","1080p30"), ("1080p60","1080p60"),("4K30","4K30"),("4K60","4K60"),)
	max_resolution  = models.CharField(max_length=10, choices=resolution_choices,default='1080p60')

	videotype_choices = (("VGA","VGA"), ("DVI","DVI"),("HDMI","HDMI"),("DisplayPort","DisplayPort"),)
	videotype = models.CharField(max_length=15, choices=videotype_choices, default='Optimized')

	compression_choices = (("Losless","Losless/Uncompressed"), ("Optimized","Optimized/Compressed"),)
	compression = models.CharField(max_length=10, choices=compression_choices, default='Optimized')

	videowall_choices = (("NotAvailable","Not available"), ("8x8","8x8"),("16x16","16x16"),("Unlimited","Unlimited"),)
	max_videowall = models.CharField(max_length=30, choices=videowall_choices)

	multiview = models.BooleanField(default=False)

	displayport_mst = models.BooleanField("DisplayPort Multi-Stream Transport",default=False)

	hdr = models.BooleanField("HDR", default=False)

# Network attributes
	interface_choices = (("1GbE","1 GbE"), ("10GbE","10 GbE"), ("Proprietary","Proprietary/Non-IP"),)
	interface = models.CharField(max_length=40, choices=interface_choices)

	port_redundancy = models.BooleanField(default=False, help_text='Select if the endpoint have more than 1 port for DATA TRANSFER')

	poe = models.BooleanField("PoE support", default=False)

	over_the_wan_support = models.BooleanField("Over-the-WAN support", default=False)

	media_type = models.ManyToManyField(NetworkMediaType, help_text='Select ALL that apply')

	access_to_virtual_sources = models.ManyToManyField(AccessToVirtualResources, help_text='Select ALL that apply')

# Audio/USB/Serial attributes

	audio_type = models.ManyToManyField(AudioType, help_text='Select ALL that apply')

	usb_speed = models.PositiveIntegerField( help_text='Enter USB speed in Mbps')

	serial_routing = models.BooleanField(default=False, help_text='Select if the endpoint can route Serial data (i.e. RS232 etc.)')
	infrared_routing = models.BooleanField(default=False)

	# def get_absolute_url(self):
	# 	return reverse("products:product_detail", kwargs={"id": self.id})
	# 	# return f"/product/{self.id}"

	def __str__(self):
		return self.sku


	def get_absolute_url(self):
		return reverse("endpoints:endpoint_detail", kwargs={"sku": self.sku})

	def main_image_tag(self):
		return mark_safe('<img src="%s" width="50" height = "50"/>' % (self.main_image.url))

	