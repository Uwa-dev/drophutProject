from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .models import BlogPost
from .models import Wishlist
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
  return render(request, 'drophutApp/base.html')

@login_required
def index(request):
  products = Product.objects.all()
  return render(request, 'drophutApp/index.html', {'products': products})

@login_required
def product_details(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'drophutApp/product_details.html', {'product': product})

@login_required
def about(request):
  return render(request, 'drophutApp/about.html')

@login_required
def blog(request):
  blog_posts = BlogPost.objects.all()
  return render(request, 'drophutApp/blog.html', {'blog_posts': blog_posts})

@login_required
def blog_details(request, blog_id):
  blog_post = get_object_or_404(BlogPost, id=blog_id)
  recent_posts = BlogPost.objects.all().order_by('-created_at')[:3]
  return render(request, 'drophutApp/blog-details.html', {'blog_post': blog_post, 'recent_posts': recent_posts})

@login_required
def faq(request):
  return render(request, 'drophutApp/faq.html')


@login_required
def privacy_policy(request):
  return render(request, 'drophutApp/privacy-policy.html')

@login_required
def contact(request):
  return render(request, 'drophutApp/contact.html')

@require_http_methods(["GET", "POST"])
def cart(request):
  products = Product.objects.all()
  cart_items = request.session.get('cart', [])

  if request.method == 'POST':
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    cart_items.append(product_id)
    request.session['cart'] = cart_items

  return render(request, 'cart.html', {'products': products, 'cart_items': cart_items})

@require_http_methods(["GET", "POST"])
def remove_from_cart(request, product_id):
  cart_items = request.session.get('cart', [])
  cart_items.remove(product_id)
  request.session['cart'] = cart_items
  return redirect('cart')

@login_required
def tracking(request):
  return render(request, 'drophutApp/tracking.html')

@login_required
def wishlist(request):
  wishlist_items = Wishlist.objects.filter(user=request.user)
  return render(request, 'drophutApp/wishlist.html', {'wishlist_items': wishlist_items})


