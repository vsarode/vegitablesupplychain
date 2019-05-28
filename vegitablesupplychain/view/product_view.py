from marshmallow import fields

from vegitablesupplychain.constants.file_path import FILE_PATH, DOWNLOAD_PATH
from vegitablesupplychain.view.base_schema import SchemaRender



class ProductView(SchemaRender):
    id = fields.Integer(dump_to='productId')
    product_name = fields.String(dump_to="productName")
    default_image = fields.Method('get_image', dump_to="productImage")
    features = fields.String()
    price = fields.Float()

    def get_image(self, obj):
        return DOWNLOAD_PATH+obj.default_image



class ProductNameView(SchemaRender):
    product_name = fields.String(dump_to="productName")
