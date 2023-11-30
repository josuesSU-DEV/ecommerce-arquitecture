from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem, Order
from products.models import Product


def show_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)
    context = {"carrito": cart, "items": items}
    return render(request, "cart/show_cart.html", context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    item, created = CartItem.objects.get_or_create(
        product=product, cart=cart, defaults={"quantity": 1}
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("show_cart")
