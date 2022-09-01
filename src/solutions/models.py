from django.db import models

# Create your models here.
class UserBasedAccess(models.Model):

	user_based_access = models.CharField(max_length=30)
	def __str__(self):
		return self.user_based_access

class Solution(models.Model):
	
# Main attributes
	title 		= models.SlugField(max_length=20)
	description = models.TextField(blank=True, null=True, max_length=1000 ,default='This Description will appear on the Solution`s page')
	summary 	= models.TextField(default='This summary will appear in the Compare page', max_length=100)
	# main_image	= models.ImageField(upload_to='media/images/')
	# front_image	= models.ImageField(upload_to='media/images/')
	# back_image	= models.ImageField(upload_to='media/images/')

	protocol_choices = (("IP","over IP"), ("Proprietary","Proprietary/Non-IP"),)
	protocol = models.CharField(max_length=15, choices=protocol_choices)

	topology_choices = (("Distributed","Distributed"), ("Chassis","Central Chassis"),)
	topology = models.CharField(max_length=15, choices=topology_choices)

	videowall_support = models.BooleanField(default=False)
	hdcp_support		= models.BooleanField(default=False)
	independent_audio_usb_serial_routing	= models.BooleanField(default=False)

	controller_redundancy = models.BooleanField(default=True)
	snmp_support = models.BooleanField(default=False)
	syslog_support = models.BooleanField(default=False)
	user_based_access = models.ManyToManyField(UserBasedAccess, blank=True,)

	def __str__(self):
		return self.title