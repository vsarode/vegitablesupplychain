from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender

class AddressView(SchemaRender):
    id = fields.Integer(dump_to="addressId")
    address_line1 = fields.String()
    address_line2 = fields.String()
    state = fields.String()
    district = fields.String()
    taluka = fields.String()
    village = fields.String()
    pincode = fields.String()


class UserView(SchemaRender):
    username = fields.String()
    fullname = fields.String(dump_to="fullName")
    account_no = fields.String(dump_to="accountNumber")
    pan_no = fields.String(dump_to="panNumber")
    user_type = fields.String(dump_to="userType")
    mobile = fields.String()
    photo = fields.String()
    shipping_addresses = fields.Method('get_addresses',dump_to="shippingAddresses")
    def get_addresses(self,obj):
        addresses = obj.shipping_addresses.all()
        view = AddressView()
        return [view.render(item) for item in addresses]



class UserNameView(SchemaRender):
    username = fields.String()


class FarmerView(SchemaRender):
    user = fields.Nested(UserView)


class HotelUserView(SchemaRender):
    user = fields.Nested(UserView)
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")


class HotelNameView(SchemaRender):
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")
