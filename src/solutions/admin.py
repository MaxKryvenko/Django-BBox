from django.contrib import admin

# Register your models here.
from .models import Solution, UserBasedAccess



class SolutionAdmin(admin.ModelAdmin):
	list_display=('title','id','protocol','topology')
	# list_editable=('max_resolution',)
admin.site.register(Solution, SolutionAdmin)

class UserBasedAccessAdmin(admin.ModelAdmin):
	list_display=('user_based_access','id',)
	list_display_links=('user_based_access','id',)
	# list_editable=('user_based_access',)
admin.site.register(UserBasedAccess, UserBasedAccessAdmin)