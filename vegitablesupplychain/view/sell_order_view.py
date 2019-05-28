import django;
from marshmallow import fields

from vegitablesupplychain.constants.file_path import DOWNLOAD_PATH

django.setup()
from vegitablesupplychain.db.supplychainmodels.models import SellOrders
from vegitablesupplychain.view.base_schema import SchemaRender, DateTimeEpoch
from vegitablesupplychain.view.product_view import ProductView
from vegitablesupplychain.view.user_view import AddressView, FarmerView


class SellOrderView(SchemaRender):
    sell_order_token = fields.String(dump_to='id')
    farmer = fields.Nested(FarmerView, dump_to="farmerDetails")
    product = fields.Nested(ProductView)
    quantity = fields.Integer()
    product_image = fields.Method('get_image')
    quality = fields.String()
    price = fields.Float()
    total_price = fields.Float(dump_to="totalPrice")
    is_shipped = fields.Boolean(dump_to="isShipped")
    created_on = DateTimeEpoch(dump_to="createdOn")
    order_status = fields.String(dump_to="orderStatus")
    shipping_address = fields.Nested(AddressView, dump_to="shippingAddress")

    def get_image(self, obj):
        return DOWNLOAD_PATH + obj.product_image


if __name__ == '__main__':
    sale_order = SellOrders.objects.first()
    view = SellOrderView()
    import json

    print json.dumps(view.render(sale_order))
