from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp' #updated
	search_fields = ['title', 'description']
	list_display = ['__unicode__', 'title', 'price', 'active', 'update']
	list_editable = ['price', 'active']
	list_filter = ['price', 'active']
	readonly_fields = ['update', 'timestamp']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)