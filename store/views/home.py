from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        print(f"cart {cart}")
        if cart:
            print('Cart --')
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')

    def get(self, request):

        cart = request.session.get('cart')
        print(f"cart - {cart}")
        if not cart:
            request.session.cart = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_product_by_categoryid(categoryID)
        else:
            products = Product.get_all_product()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are : ', request.session.get('email'))
        return render(request, 'index.html', data)
        # response = get_response
