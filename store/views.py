from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product
# Create your views here.
def store(request,category_slug=None):
  products=None
  category=None  
  if category_slug != None:
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(is_available=True,category=category)
  else:
    products = Product.objects.filter(is_available=True)
  context={'products':products,
           'product_count':products.count()}
  return render(request,"store/store.html",context)

def product_detail(request,category_slug,product_slug):
  try:
    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
  except Exception as e:
    raise e
  
  context = {"single_product":single_product}
  return render(request,'store/product_detail.html',context)