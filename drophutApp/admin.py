from django.contrib import admin
from .models import Product
from .models import ProductReview
from .models import BlogPost

admin.site.site_header = 'Drophut shop admin'
admin.site.site_title = 'Drophut shop admin portal'
admin.site.index_title = 'Welcome to Drophut shop Admin'

def mark_as_out_of_stock(modeladmin, request, queryset):
  queryset.update(stock=0)

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'description', 'stock')
  list_editable = ('price', 'stock')
  search_fields = ('name', 'description')
  actions = [mark_as_out_of_stock]
  list_per_page = 10

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview)
admin.site.register(BlogPost)

