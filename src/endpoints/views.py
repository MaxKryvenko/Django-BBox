from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.urls import reverse

# from .forms import EndpointForm
from .models import Endpoint
# Create your views here.


class EndpointListView(ListView):	# By default Class-based view is looking for "<app_name>/<model_name>_<view_name>.html" TEMPLATE such as the file:"blog/article_list.html"
	paginate_by = 4
	model = Endpoint
	#template_name = 'blog/article_list.html'
	# queryset = {'endpoints' : Endpoint.objects.all(), 'switching controls' : Endpoint.objects.distinct().values('switching_control__switching_control')}
	# queryset = Endpoint.objects.all()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['switching_control'] = Endpoint.objects.distinct().values('switching_control__switching_control','switching_control__id')
		#media_type
		context['media_type'] = Endpoint.objects.distinct().values('media_type__media_type','media_type__id')
		return context

class EndpointDetailView(DetailView):	
	
	queryset = Endpoint.objects.all()

	def get_object(self):
		sku_ = self.kwargs.get("sku")
		return get_object_or_404(Endpoint, sku=sku_)