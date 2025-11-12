
from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=100)
	company = models.CharField(max_length=150, blank=True)
	email = models.EmailField()
	mobile = models.CharField(max_length=20, blank=True)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} <{self.email}>"



from django.db.models import JSONField


class Product(models.Model):
	id = models.SlugField(primary_key=True, max_length=100)
	title = models.CharField(max_length=200, blank=True, null=True)
	short_description = models.CharField(max_length=300, blank=True, null=True)
	full_description = models.TextField(blank=True, null=True)
	icon = models.CharField(max_length=100, blank=True, null=True)
	specifications = JSONField(blank=True, null=True, default=list)
	applications = JSONField(blank=True, null=True, default=list)
	key_features = JSONField(blank=True, null=True, default=list)
	technical_details = JSONField(blank=True, null=True, default=list)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
