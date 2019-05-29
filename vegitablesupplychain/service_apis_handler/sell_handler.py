import uuid

from vegitablesupplychain.db.supplychainmodels.models import SellOrders, Cart
from vegitablesupplychain.service_apis_handler import product_handler, \
    user_handler
from vegitablesupplychain.utils.exceptions import NotFoundException
from vegitablesupplychain.view.sell_order_view import SellOrderView


def place_sell_order(request_data):
    farmer_obj = user_handler.get_user_profile(request_data['userId'])
    order_obj = SellOrders.objects.create(farmer=farmer_obj,
                                          sell_order_token=str(uuid.uuid4()),
                                          product=product_handler.get_product_by_id(
                                              request_data['productId']),
                                          quality = request_data['quality'],
                                          quantity=request_data['quantity'],
                                          product_image=request_data[
                                              'productPic'],
                                          price=request_data[
                                              'price'],
                                          total_price=float(request_data[
                                              'price'])*int(request_data['quantity']))

    return order_obj

def get_order_response_for_hotel(order_obj, hotel_object):
    view = SellOrderView()
    res = view.render(order_obj)
    sale_orders = Cart.objects.filter(hotel=hotel_object)[0].cart_items.all() if Cart.objects.filter(hotel=hotel_object) else []
    sell_order_to_cart_map = {ci.sell_order.sell_order_token: True for ci in sale_orders}
    if order_obj.sell_order_token in sell_order_to_cart_map:
        res['isInCart'] = True
    else:
        res['isInCart'] = False
    return res

def get_order_by_username(username):
    try:
        obj = user_handler.get_user_profile(username)
        sale_orders = SellOrders.objects.filter(farmer=obj)
        print sale_orders
        return sale_orders
    except:
        raise NotFoundException(entity='Order')


def get_order_by_filter(criteria={}):
    try:
        return SellOrders.objects.filter(**criteria)
    except:
        raise NotFoundException(entity='Order')


def get_order_by_token(token):
    try:
        return SellOrders.objects.get(sell_order_token=token)
    except:
        raise NotFoundException(entity='Order')


def update_shipping_address(order_obj, request_data):
    order_obj.shipping_address = user_handler.get_address_object_by_id(
        request_data['addressId'])


def get_in_stock_products(data):
    filter = {'order_status': 'In Stock'}
    if 'productId' in data:
        filter['product_id'] = data['productId']

    sell_orders = SellOrders.objects.filter(**filter)
    return sell_orders
