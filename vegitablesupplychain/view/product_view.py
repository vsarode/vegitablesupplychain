from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender

class CategoryView(SchemaRender):
    category_name = fields.String(dump_to="categoryName")


class BrandView(SchemaRender):
    brand_name = fields.String(dump_to="brandName")


class ProductView(SchemaRender):
    id = fields.Integer(dump_to='productId')
    product_name = fields.String(dump_to="productName")
    category = fields.Nested(CategoryView)
    brand = fields.Nested(BrandView)
    default_image = fields.String(dump_to="productImage")
    features = fields.String()
    price = fields.Float()


class ProductNameView(SchemaRender):
    product_name = fields.String(dump_to="productName")