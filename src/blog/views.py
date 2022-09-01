from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.urls import reverse

from .forms import ArticleForm
from .models import Article
# Create your views here.


class ArticleListView(ListView):	# By default Class-based view is looking for "<app_name>/<model_name>_<view_name>.html" TEMPLATE such as the file:"blog/article_list.html"
	paginate_by = 2
	#template_name = 'blog/article_list.html'
	queryset = Article.objects.all()


class ArticleDetailView(DetailView):	
	
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
		template_name = 'blog/article_create.html'
		queryset = Article.objects.all() 
		form_class = ArticleForm


		def form_valid(self, form):
			print(form.cleaned_data)
			return super().form_valid(form)


class ArticleUpdateView(UpdateView):
		template_name = 'blog/article_create.html'
		queryset = Article.objects.all() 
		form_class = ArticleForm

		def form_valid(self, form):
			print(form.cleaned_data)
			return super().form_valid(form)

		def get_object(self):
			id_ = self.kwargs.get("id")
			return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):	
	
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('articles:article_list')