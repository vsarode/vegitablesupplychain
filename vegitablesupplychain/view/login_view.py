from marshmallow import fields

from vegitablesupplychain.db.supplychainmodels.models import Farmer, Hotel, Cart
from vegitablesupplychain.view.base_schema import SchemaRender, DateTimeEpoch
from vegitablesupplychain.view.user_view import UserView


class LoginView(SchemaRender):
    user = fields.Nested(UserView)
    login_token = fields.String()
    created_on = DateTimeEpoch(dump_to="loggedInTime")
    loggedout_time = DateTimeEpoch(dump_to="loggedOutTime")
    is_logged_in = fields.Boolean(dump_to="isLoggedIn")
    cartItems = fields.Method('get_cart', dump_to='cartItems')
    userType = fields.Method('get_user_type')

    def get_user_type(self, obj):
        return 'Farmer' if Farmer.objects.filter(
            user_id=obj.user.username) else 'Hotel'

    def get_cart(self, obj):
        try:
            hotel = Hotel.objects.get(user_id=obj.user_id)
        except:
            return 0
        cart = Cart.objects.filter(hotel=hotel, is_active=True)
        if cart:
            return cart[0].cart_items.all().count()
        else:
            return 0
