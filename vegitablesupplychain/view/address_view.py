from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender


class AddressView(SchemaRender):
    address_line1 = fields.String()
    address_line2 = fields.String()
    state = fields.String()
    district = fields.String()
    taluka = fields.String()
    village = fields.String()
    pincode = fields.String()



