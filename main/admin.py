
from django.contrib import admin
from .models import Contact, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ContactResource(resources.ModelResource):
	class Meta:
		model = Contact

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
	resource_class = ContactResource
	list_display = ("name", "email", "created_at")
	search_fields = ("name", "email")


class ProductResource(resources.ModelResource):
	class Meta:
		model = Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
	resource_class = ProductResource
	list_display = ("id", "title", "created_at")
	search_fields = ("id", "title")
