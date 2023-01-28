from django.shortcuts import render , redirect
from django.urls import reverse

from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        # print(products)
        return render(request , 'cart.html' , {'products' : products} )


def remove_from_cart(request, id):
        try:
            # print('id',id)
            del request.session['cart'][id]
            request.session.modified = True
            # print(product_id)
            # cart= Product.objects.get(id=id)
            # cartitem = Product.objects.filter(id=id).delete()
            # cartitem.cart = None
            # cartitem.save()
        except Exception as e:
            
            return redirect('cart')

        
        
        # cartitem.delete()
        print('id',id)
        return redirect('cart')



        


        

