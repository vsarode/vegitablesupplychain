from vegitablesupplychain.db.supplychainmodels.models import CartItem
from vegitablesupplychain.service_apis_handler import sell_handler
from vegitablesupplychain.utils.exceptions import NotFoundException, \
    GenericCustomException


def create_cart_item(data):
    sell_order_object = sell_handler.get_order_by_token(
        data['sellOrderToken'])
    if sell_order_object.order_status != 'In Stock':
        raise GenericCustomException(message='Item out of stock')
    cart_item_object = CartItem.objects.create(sell_order=sell_order_object,
                                               price=sell_order_object.price)
    sell_order_object.is_shipped=True
    sell_order_object.save()
    return cart_item_object


def get_cart_item_by_id(cart_item_id):
    try:
        return CartItem.objects.get(id=cart_item_id)
    except:
        raise NotFoundException(entity='Cart item')
