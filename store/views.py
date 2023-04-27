from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product
from cart.forms import CartAddProductForm
# from django.contrib.postgres.search import SearchVector
# from haystack.query import SearchQuerySet
from store.forms import SearchForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(
            Category, 
            slug=category_slug)
        products = products.filter(category=category)

    return render(request,
        'store/product/list.html',
        {'category': category,
        'categories': categories,
        'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
        'store/product/detail.html',
        {'product': product,
         'cart_product_form': cart_product_form})



def product_search(request):
    query = request.GET.get('query')
    products = []

    if query:
        query_list = query.split()
        q = Q()
        for word in query_list:
            q |= Q(name__icontains=word) | Q(description__icontains=word)
        products = Product.objects.filter(q)

    form = SearchForm(initial={'search_query': query})

    context = {
        'form': form,
        'products': products,
        'query': query,
    }

    return render(request, 'store/product/search.html', context)