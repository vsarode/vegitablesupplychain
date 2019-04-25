from vegitablesupplychain.db.supplychainmodels.models import PurchaseOrders, \
    CartItem, SellOrders
from vegitablesupplychain.service_apis_handler import product_handler, \
    user_handler, login_handler, cart_handler
from vegitablesupplychain.utils.exceptions import NotFoundException
from vegitablesupplychain.view.order_view import PurchaseOrderView


def place_purchase_order(request_data):
    hotel_obj = user_handler.get_user_profile(request_data['userId'])
    cart_obj = cart_handler.get_cart_for_hotel(hotel_obj.user.username)

    purchase_order_obj = PurchaseOrders.objects.create(hotel=hotel_obj,cart=cart_obj,
                                              total_price=request_data[
                                                  'totalPrice'],
                                              shipping_address=user_handler.get_address_object_by_id(
                                                  request_data['addressId']))
    post_purchase_order_action(cart_obj)
    return purchase_order_obj


def post_purchase_order_action(cart_obj):
    for item in cart_obj.cart_items.all():
        try:
            sell_obj = SellOrders.objects.get(sell_order_token=item.sell_order.sell_order_token)
            sell_obj.quantity -= item.quantity
            sell_obj.save()
            if sell_obj.quantity == 0:
                sell_obj.order_status = 'Sold Out'
                sell_obj.save()
        except:
            raise NotFoundException(entity='Product')


def delete_purchase_order_action(order_obj):
    cart_obj = order_obj.cart
    for item in cart_obj.cart_items.all():
        try:
            sell_obj = SellOrders.objects.get(id=item.sell_order.id)
            if sell_obj.quantity == 0:
                sell_obj.order_status = 'In Stock'
            sell_obj.quantity += item.quantity
            sell_obj.save()
        except:
            raise NotFoundException(entity='Product')

def get_order_json(order_obj):
    view = PurchaseOrderView()
    return view.render(order_obj)


def get_order_by_username(username):
    try:
        obj = user_handler.get_user_profile(username)
        return PurchaseOrders.objects.filter(
            hotel=obj)
    except:
        raise NotFoundException(entity='Order')


def get_order_by_filter(criteria={}):
    try:
        return PurchaseOrders.objects.filter(**criteria)
    except:
        raise NotFoundException(entity='Order')


def get_order_by_token(token):
    try:
        return PurchaseOrders.objects.get(purchase_order_token=token)
    except:
        raise NotFoundException(entity='Order')


def update_shipping_address(order_obj, request_data):
    order_obj.shipping_address = user_handler.get_address_object_by_id(
        request_data['addressId'])
