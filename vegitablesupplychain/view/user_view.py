from marshmallow import fields

from vegitablesupplychain.view.address_view import AddressView
from vegitablesupplychain.view.base_schema import SchemaRender


class UserView(SchemaRender):
    username = fields.String()
    fname = fields.String(dump_to="firstName")
    mname = fields.String(dump_to="middleName")
    lname = fields.String(dump_to="lastName")
    usertype = fields.String(dump_to="userType")
    mobile = fields.String()
    gender = fields.String()
    address = fields.Nested(AddressView)

class UserNameView(SchemaRender):
    username = fields.String()

class HotelUserView(SchemaRender):
    user = fields.Nested(UserView)
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")



