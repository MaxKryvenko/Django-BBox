from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='your title', 
							widget=forms.TextInput(attrs={"placeholder":"Your title","class": "my_class"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"write you description", "rows": 20}))

	price = forms.DecimalField(initial=199.90)

	class Meta:
		model = Product
		fields = ['title', 'description', 'price']

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		print(title)
		if not "max" in title:
			raise ValidationError('This is not a valid title')
		if not title.endswith("abc"):
			raise ValidationError('This is not a valid title')
		return title
