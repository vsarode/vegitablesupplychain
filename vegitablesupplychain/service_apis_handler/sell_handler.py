import uuid

from vegitablesupplychain.db.supplychainmodels.models import CartItem, \
    SellOrders
from vegitablesupplychain.service_apis_handler import product_handler, \
    user_handler, login_handler
from vegitablesupplychain.utils.exceptions import NotFoundException
from vegitablesupplychain.view.order_view import SellOrderView


def place_sell_order(request_data):
    farmer_obj = user_handler.get_user_profile(request_data['userId'])
    order_obj = SellOrders.objects.create(farmer=farmer_obj,
                                          sell_order_token=uuid.uuid4(),
                                          product=product_handler.get_product_by_id(request_data['productId']),
                                          quantity=request_data['quantity'],
                                          product_image=request_data['productPic'],
                                          total_price=request_data[
                                              'totalPrice'],
                                          shipping_address=user_handler.get_address_object_by_id(
                                              request_data['addressId']))

    return order_obj


def get_order_json(order_obj):
    view = SellOrderView()
    return view.render(order_obj)


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


def get_in_stock_products():
    sell_orders = SellOrders.objects.filter(order_status='In Stock')
    return sell_orders