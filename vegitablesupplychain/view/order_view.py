from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender, DateTimeEpoch
from vegitablesupplychain.view.cartitem_view import CartItemView
from vegitablesupplychain.view.user_view import HotelNameView, AddressView


class CartView(SchemaRender):
    id = fields.String('id')
    hotel = fields.Nested(HotelNameView)
    cart_items = fields.Method('get_cart_items', dump_to='cartItems')
    is_active = fields.Boolean(dump_to='isActive')
    created_on = DateTimeEpoch(dump_to='createdOn')
    total_item_price = fields.Float(dump_to='totalPrice')

    def get_cart_items(self, obj):
        cart_items = obj.cart_items.all()
        view = CartItemView()
        return [view.render(item) for item in cart_items]


class PurchaseOrderView(SchemaRender):
    purchase_order_token = fields.String()
    hotel = fields.Nested(HotelNameView, dump_to="hotelDetails")
    cart = fields.Nested(CartView)
    total_price = fields.Float(dump_to="totalPrice")
    is_shipped = fields.Boolean(dump_to="isShipped")
    created_on = DateTimeEpoch(dump_to="createdOn")
    shipping_address = fields.Nested(AddressView, dump_to="shippingAddress")
