from marshmallow import fields

from vegitablesupplychain.constants.file_path import FILE_PATH, DOWNLOAD_PATH
from vegitablesupplychain.view.base_schema import SchemaRender


class CategoryView(SchemaRender):
    category_name = fields.String(dump_to="categoryName")


class BrandView(SchemaRender):
    brand_name = fields.String(dump_to="brandName")


class ProductView(SchemaRender):
    id = fields.Integer(dump_to='productId')
    product_name = fields.String(dump_to="productName")
    category = fields.Method("get_category")
    brand = fields.Method("get_brand")
    default_image = fields.Method('get_image', dump_to="productImage")
    features = fields.String()
    price = fields.Float()

    def get_image(self, obj):
        return DOWNLOAD_PATH+obj.default_image

    def get_brand(self, obj):
        return obj.brand.brand_name

    def get_category(self, obj):
        return obj.category.category_name


class ProductNameView(SchemaRender):
    product_name = fields.String(dump_to="productName")
