from vegitablesupplychain.db.supplychainmodels.models import CartItem, \
    SellOrders
from vegitablesupplychain.service_apis_handler import product_handler, \
    user_handler, login_handler
from vegitablesupplychain.utils.exceptions import NotFoundException
from vegitablesupplychain.view.order_view import SellOrderView


def place_sell_order(request_data):
    if 'userId' in request_data:
        farmer_obj = user_handler.get_user_profile(request_data['userId'])
    elif 'token' in request_data:
        farmer_obj = login_handler.get_user_object_by_token(
            request_data['token'])
    # print user_handler.get_user_json(farmer_obj)
    order_obj = SellOrders.objects.create(farmer=farmer_obj,
                                          total_price=request_data[
                                              'totalPrice'],
                                          shipping_address=user_handler.get_address_object_by_id(
                                              request_data['addressId']))
    map(lambda cart_item: order_obj.cart_items.add(cart_item),
        create_cart_with_items(request_data))
    # for cart_item in create_cart_with_items(request_data):
    #     order_obj.add(cart_item)
    order_obj.save()
    return order_obj


def create_cart_with_items(request_data):
    cart_items = request_data['cartItems']
    items_obj = [create_cart_item(cart_items.get(item)) for item in cart_items]
    return items_obj


def update_cart_items(order_obj, request_data):
    order_obj.cart_items.clear()
    order_obj.cart_items.add(*create_cart_with_items(request_data))


def create_cart_item(item):
    return CartItem.objects.create(
        product=product_handler.get_product_by_name(item['productName']),
        quantity=item['quantity'],
        price=item['price'])


def get_order_json(order_obj):
    view = SellOrderView()
    return view.render(order_obj)


def get_order_by_username(username):
    try:
        obj = user_handler.get_user_profile(username)
        return SellOrders.objects.filter(
            farmer=obj)
    except:
        raise NotFoundException()


def get_order_by_filter(criteria={}):
    try:
        return SellOrders.objects.filter(**criteria)
    except:
        raise NotFoundException()


def get_order_by_token(token):
    try:
        return SellOrders.objects.get(sell_order_token=token)
    except:
        raise NotFoundException()


def update_shipping_address(order_obj, request_data):
    order_obj.shipping_address = user_handler.get_address_object_by_id(
        request_data['addressId'])
