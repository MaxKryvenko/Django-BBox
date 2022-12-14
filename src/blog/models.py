from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	author = models.CharField(max_length=120)
	body = models.TextField()
	email = models.EmailField()

	def get_absolute_url(self):
		return reverse("articles:article_detail", kwargs={"id": self.id})
