from flask import request

from vegitablesupplychain.service_apis_handler import user_handler, \
    login_handler
from vegitablesupplychain.utils.resource import BaseResource
from vegitablesupplychain.view.user_view import AddressView


class AddressApi(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        username = request_data['userId']
        user_obj = user_handler.get_user_profile(username)
        obj = user_handler.create_address_object(request_data['address'])
        user_obj.user.shipping_addresses.add(obj)
        view = AddressView()
        return {"address": view.render(obj)}

    def get(self):
        data = request.args
        username = data['userId']
        view = AddressView()

        if username:
            addresses = user_handler.get_addresses_by_username(username)
            return {
                "address": [view.render(adr) for
                            adr
                            in addresses]}
        token = request.headers.get('token')

        if token:
            user_obj = login_handler.get_user_object_by_token(token)
            addresses = user_handler.get_addresses_by_username(
                user_obj.user.username)
            return {
                "address": [view.render(adr) for
                            adr
                            in addresses]}
        address_id = data.get('addressId')
        if address_id:
            address_obj = user_handler.get_address_object_by_id(address_id)
            return {'address': view.render(address_obj)}

    def put(self, id):
        request_data = request.get_json(force=True)
        address = user_handler.update_address_of_user(id, request_data)
        view = AddressView()
        return {"address": view.render(address)}
