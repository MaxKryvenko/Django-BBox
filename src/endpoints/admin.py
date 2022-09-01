from django.contrib import admin

# Register your models here.
from .models import Endpoint, SwitchingControl, NetworkMediaType, AccessToVirtualResources, AudioType



class EndpointAdmin(admin.ModelAdmin):
	list_display=('sku','id','solution','status','endpoint_mode','videotype','max_resolution', 'main_image_tag',)#,'created_by','native_in_out')

	# fieldsets = ((''))
	list_editable=('status',)
admin.site.register(Endpoint, EndpointAdmin)

class SwitchingControlAdmin(admin.ModelAdmin):
	pass
admin.site.register(SwitchingControl, SwitchingControlAdmin)

class NetworkMediaTypeAdmin(admin.ModelAdmin):
	pass
admin.site.register(NetworkMediaType, NetworkMediaTypeAdmin)

class AccessToVirtualResourcesAdmin(admin.ModelAdmin):
	pass
admin.site.register(AccessToVirtualResources, AccessToVirtualResourcesAdmin)

class AudioTypeAdmin(admin.ModelAdmin):
	pass
admin.site.register(AudioType, AudioTypeAdmin)