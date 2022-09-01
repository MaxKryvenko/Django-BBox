from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
	print(args)
	print(kwargs)
	my_context={"my_text":"this is a context text","my_number":123,"my_list":["a","b","c"],}
	return render(request, "home.html", my_context)