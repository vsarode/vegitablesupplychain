from flask import request

from vegitablesupplychain.service_apis_handler import user_handler, login_handler
from vegitablesupplychain.utils.resource import BaseResource


class AddressApi(BaseResource):
    def post(self, username=None):
        request_data = request.get_json(force=True)
        if username:
            user_obj = user_handler.get_user_profile(username)
            obj = user_handler.create_address_object(request_data)
            user_obj.user.shipping_addresses.add(obj)
            return user_handler.get_address_json(obj)
        token = request.headers.get('token')
        if token:
            user_obj = login_handler.get_user_object_by_token(token)
            obj = user_handler.create_address_object(request_data)
            user_obj.user.shipping_addresses.add(obj)
            return user_handler.get_address_json(obj)

    def get(self, username=None):
        if username:
            addresses = user_handler.get_addresses_by_username(username)
            return {
                "shippingAddresses": [user_handler.get_address_json(adr) for
                                      adr
                                      in addresses]}
        token = request.headers.get('token')
        if token:
            user_obj = login_handler.get_user_object_by_token(token)
            addresses = user_handler.get_addresses_by_username(user_obj.user.username)
            return {
                "shippingAddresses": [user_handler.get_address_json(adr) for
                                      adr
                                      in addresses]}

    def put(self, username=None):
        request_data = request.get_json(force=True)
        if username:
            addresses = user_handler.update_addresses_of_user(username,
                                                                 request_data)
            return {
                "shippingAddresses": [user_handler.get_address_json(adr) for
                                      adr
                                      in addresses]}
        token = request.headers.get('token')
        if token:
            user_obj = login_handler.get_user_object_by_token(token)
            addresses = user_handler.update_address_of_user(user_obj.user.username,
                                                               request_data)
            return {
                "shippingAddresses": [user_handler.get_address_json(adr) for
                                      adr
                                      in addresses]}
