from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender, DateTimeEpoch
from vegitablesupplychain.view.product_view import ProductView
from vegitablesupplychain.view.user_view import HotelNameView, AddressView, \
    FarmerView


class CartItemView(SchemaRender):
    product = fields.Nested(ProductView,dump_to="productDetails")
    price = fields.Float()
    quantity = fields.Integer()


class PurchaseOrderView(SchemaRender):
    purchase_order_token = fields.String()
    hotel = fields.Nested(HotelNameView,dump_to="hotelDetails")
    cart_items = fields.Method('get_cart_items',dump_to="cartItems")
    total_price = fields.Float(dump_to="totalPrice")
    is_shipped = fields.Boolean(dump_to="isShipped")
    created_on = DateTimeEpoch(dump_to="createdOn")
    shipping_address = fields.Nested(AddressView,dump_to="shippingAddress")

    def get_cart_items(self,obj):
        cart_items = obj.cart_items.all()
        view = CartItemView()
        return [view.render(item) for item in cart_items]


class SellOrderView(SchemaRender):
    sell_order_token = fields.String()
    farmer = fields.Nested(FarmerView,dump_to="farmerDetails")
    cart_items = fields.Method('get_cart_items',dump_to="cartItems")
    total_price = fields.Float(dump_to="totalPrice")
    is_shipped = fields.Boolean(dump_to="isShipped")
    created_on = DateTimeEpoch(dump_to="createdOn")
    shipping_address = fields.Nested(AddressView,dump_to="shippingAddress")

    def get_cart_items(self,obj):
        cart_items = obj.cart_items.all()
        view = CartItemView()
        return [view.render(item) for item in cart_items]
