from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_detail_view(request, id):
	
	# obj = Product.objects.get(id=id)
	obj = get_object_or_404(Product, id=id)
	context = {
	'object': obj,
	}
	
	return render(request, "products/product_detail.html",context)



def product_create_view(request):
	#initial_data = {'title': 'ProdX', 'price': 101.92}
	#obj=Product.objects.get(id=1)
	form = ProductForm(request.POST or None)#, instance=obj)
	if form.is_valid():
		form.save()
		# form = ProductForm(instance=obj)
	context = {
	'form': form
	}
	
	return render(request, "products/product_create.html",context)


def product_list_view(request):
	queryset = Product.objects.all()
	context = {"object_list":queryset}

	return render(request, "products/product_list.html", context)