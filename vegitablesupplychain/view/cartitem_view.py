from vegitablesupplychain.view.base_schema import SchemaRender
from marshmallow import fields

from vegitablesupplychain.view.sell_order_view import SellOrderView


class CartItemView(SchemaRender):
    id = fields.Integer()
    sell_order = fields.Nested(SellOrderView, dump_to="productDetails")
    price = fields.Float()
    quantity = fields.Integer()
