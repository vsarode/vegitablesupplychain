from vegitablesupplychain.db.supplychainmodels.models import Cart
from vegitablesupplychain.service_apis_handler import user_handler, \
    cart_item_handler
from vegitablesupplychain.utils.exceptions import NotFoundException


def create_cart(request_data):
    hotel_object = user_handler.get_user_profile(request_data['userId'])
    cart_item_object = cart_item_handler.create_cart_item(
        request_data['cartItem'])
    cart_object, _ = Cart.objects.get_or_create(hotel=hotel_object,
                                                is_active=True)
    cart_object.total_item_price = cart_object.total_item_price + cart_item_object.price if cart_object.total_item_price else 0 + cart_item_object.price
    cart_object.save()
    cart_object.cart_items.add(cart_item_object)
    return cart_object


def get_cart_for_hotel(username):
    try:
        hotel = user_handler.get_user_profile(username)
        return Cart.objects.get(hotel=hotel, is_active=True)
    except:
        raise NotFoundException(entity='Cart')


def handle_update(request_data, cart_object):
    action = request_data['action']
    cart_item = request_data['cartItem']
    if action == 'ADD_ITEM':
        cart_item_object = cart_item_handler.create_cart_item(cart_item)
        cart_object.cart_items.add(cart_item_object)
        cart_object.total_item_price += cart_item_object.price * cart_item_object.quantity
        cart_object.save()
        return cart_object
    cart_item_object = cart_item_handler.get_cart_item_by_id(cart_item['id'])
    if action == 'INCREASE_QUANTITY':
        cart_item_object.quantity += 1
        cart_item_object.save()
        cart_object.total_item_price = cart_object.total_item_price + cart_item_object.price  if cart_object.total_item_price else cart_item_object.price
        cart_object.save()
        return cart_object
    if action == 'DECREASE_QUANTITY':
        if cart_item_object.quantity == 1:
            cart_object.cart_items.remove(cart_item_object)
            if len(cart_object.cart_items.all()) == 0:
                cart_object.delete()
                return None
            return cart_object
        else:
            cart_item_object.quantity -= 1
            cart_item_object.save()
            cart_object.total_item_price = cart_object.total_item_price - cart_item_object.price
            cart_object.save()
            return cart_object
