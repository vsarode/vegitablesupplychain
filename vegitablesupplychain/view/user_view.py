from marshmallow import fields

from vegitablesupplychain.view.address_view import AddressView
from vegitablesupplychain.view.base_schema import SchemaRender


class UserView(SchemaRender):
    username = fields.String()
    fullname = fields.String(dump_to="fullName")
    account_no = fields.String(dump_to="accountNumber")
    pan_no = fields.String(dump_to="panNumber")
    usertype = fields.String(dump_to="userType")
    mobile = fields.String()
    photo = fields.String()
    address = fields.Nested(AddressView)


class UserNameView(SchemaRender):
    username = fields.String()


class FarmerView(SchemaRender):
    user = fields.Nested(UserView)


class HotelUserView(SchemaRender):
    user = fields.Nested(UserView)
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")



