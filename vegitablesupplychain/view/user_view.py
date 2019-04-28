from marshmallow import fields
from vegitablesupplychain.view.base_schema import SchemaRender
from vegitablesupplychain.db.supplychainmodels.models import Farmer, Hotel

class AddressView(SchemaRender):
    id = fields.Integer(dump_to="addressId")
    address_line1 = fields.String()
    address_line2 = fields.String()
    state = fields.String()
    district = fields.String()
    taluka = fields.String()
    village = fields.String()
    pincode = fields.String()


class UserBasic(SchemaRender):
    username = fields.String()
    fullname = fields.String(dump_to="fullName")
    mobile = fields.String()
    photo = fields.Method('get_profile_pic_url', dump_to='photo')

    def get_profile_pic_url(self, obj):
        return '/data/' + obj.photo


class UserView(UserBasic):
    account_no = fields.String(dump_to="accountNumber")
    pan_no = fields.String(dump_to="panNumber")
    shipping_addresses = fields.Method('get_addresses',
                                       dump_to="shippingAddresses")
    def get_addresses(self, obj):
        addresses = obj.shipping_addresses.all()
        view = AddressView()
        return [view.render(item) for item in addresses]


class UserNameView(SchemaRender):
    username = fields.String()


class FarmerView(SchemaRender):
    user = fields.Nested(UserBasic)


class FarmerFullView(SchemaRender):
    user = fields.Nested(UserView)


class HotelUserView(SchemaRender):
    user = fields.Nested(UserBasic)
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")


class HotelFullView(SchemaRender):
    user = fields.Nested(UserView)
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")


class HotelNameView(SchemaRender):
    hotel_name = fields.String(dump_to="hotelName")
    gstn_no = fields.String(dump_to="gstnNumber")


if __name__ == '__main__':
    import json

    view = UserBasic()
    import django;

    django.setup()
    from vegitablesupplychain.db.supplychainmodels.models import User, Cart, \
        Hotel, Farmer

    user = User.objects.get(username='test5@mail.com')
    print json.dumps(view.render(user))
