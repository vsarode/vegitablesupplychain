from flask import request

from vegitablesupplychain.service_apis_handler import cart_handler
from vegitablesupplychain.utils.resource import BaseResource
from vegitablesupplychain.view.order_view import CartView


class Cart(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        cart_object = cart_handler.create_cart(request_data)
        view = CartView()
        return {"cart": view.render(cart_object)}

    def get(self, username):
        cart_object = cart_handler.get_cart_for_hotel(username)
        view = CartView()
        return {"cart": view.render(cart_object)}

    def put(self, username):
        cart_object = cart_handler.get_cart_for_hotel(username)
        request_data = request.get_json(force=True)
        cart_object = cart_handler.handle_update(request_data, cart_object)
        if not cart_object:
            return {}
        view = CartView()
        return {'cart': view.render(cart_object)}
