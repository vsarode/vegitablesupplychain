from vegitablesupplychain.db.supplychainmodels.models import PurchaseOrders, \
    CartItem
from vegitablesupplychain.service_apis_handler import product_handler, \
    user_handler, login_handler
from vegitablesupplychain.utils.exceptions import NotFoundException
from vegitablesupplychain.view.order_view import PurchaseOrderView


def place_purchase_order(request_data):
    if 'userId' in request_data:
        hotel_obj = user_handler.get_user_profile(request_data['userId'])
    elif 'token' in request_data:
        hotel_obj = login_handler.get_user_object_by_token(
            request_data['token'])

    order_obj = PurchaseOrders.objects.create(hotel=hotel_obj,
                                              total_price=request_data[
                                                  'totalPrice'],
                                              shipping_address=user_handler.create_address_object(
                                                  request_data))
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


def update_cart_items(order_obj,request_data):
    order_obj.cart_items.clear()
    order_obj.cart_items.add(*create_cart_with_items(request_data))

def create_cart_item(item):
    return CartItem.objects.create(
        product=product_handler.get_product_by_name(item['productName']),
        quantity=item['quantity'],
        price=item['price'])


def get_order_json(order_obj):
    view = PurchaseOrderView()
    return view.render(order_obj)


def get_order_by_username(username):
    try:
        obj = user_handler.get_user_profile(username)
        return PurchaseOrders.objects.filter(
            hotel=obj)
    except:
        raise NotFoundException()


def get_order_by_filter(criteria={}):
    try:
        return PurchaseOrders.objects.filter(**criteria)
    except:
        raise NotFoundException()


def get_order_by_token(token):
    try:
        return PurchaseOrders.objects.get(purchase_order_token=token)
    except:
        raise NotFoundException()


def update_shipping_address(order_obj,request_data):
    order_obj.shipping_address.address_line1 = request_data['addressLine1']
    order_obj.shipping_address.address_line2 = request_data['addressLine2']
    order_obj.shipping_address.state = request_data['state']
    order_obj.shipping_address.district = request_data['district']
    order_obj.shipping_address.taluka = request_data['taluka']
    order_obj.shipping_address.village = request_data['village']
    order_obj.shipping_address.pincode = request_data['pincode']
