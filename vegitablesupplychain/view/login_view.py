from marshmallow import fields

from vegitablesupplychain.view.base_schema import SchemaRender, DateTimeEpoch
from vegitablesupplychain.view.user_view import UserView


class LoginView(SchemaRender):
    user = fields.Nested(UserView)
    login_token = fields.String()
    created_on = DateTimeEpoch(dump_to="loggedInTime")
    loggedout_time = DateTimeEpoch(dump_to="loggedOutTime")
    is_logged_in = fields.Boolean(dump_to="isLoggedIn")