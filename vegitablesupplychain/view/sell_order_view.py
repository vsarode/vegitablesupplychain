from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender, DateTimeEpoch
from vegitablesupplychain.view.product_view import ProductView
from vegitablesupplychain.view.user_view import AddressView, FarmerView


class SellOrderView(SchemaRender):
    sell_order_token = fields.String()
    farmer = fields.Nested(FarmerView, dump_to="farmerDetails")
    product = fields.Nested(ProductView)
    quantity = fields.Integer()
    product_image = fields.String()
    total_price = fields.Float(dump_to="totalPrice")
    is_shipped = fields.Boolean(dump_to="isShipped")
    created_on = DateTimeEpoch(dump_to="createdOn")
    shipping_address = fields.Nested(AddressView, dump_to="shippingAddress")
