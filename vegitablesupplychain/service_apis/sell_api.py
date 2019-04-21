from flask import request

from vegitablesupplychain.db.supplychainmodels.models import SellOrders
from vegitablesupplychain.service_apis_handler import sell_handler, user_handler
from vegitablesupplychain.utils.resource import BaseResource


class SellOrderApi(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        order = sell_handler.place_sell_order(request_data)
        return sell_handler.get_order_json(order)

    def get(self, username=None):
        if username:
            orders = sell_handler.get_order_by_username(username)
            return {
                "SellOrders": [sell_handler.get_order_json(order) for order
                               in orders]}
        token = request.headers.get('token')
        if token:
            order_obj = sell_handler.get_order_by_token(token)
            return sell_handler.get_order_json(order_obj)

    def put(self):
        request_data = request.get_json(force=True)
        token = request.headers.get('token')
        order_obj = sell_handler.get_order_by_token(token)
        order_obj.farmer = user_handler.get_user_profile(request_data['userId'])
        order_obj.total_price = request_data['totalPrice']
        order_obj.shipping_address = sell_handler.update_shipping_address(
            order_obj, request_data)
        sell_handler.update_cart_items(order_obj, request_data)
        return sell_handler.get_order_json(order_obj)

    def delete(self):
        token = request.headers.get('token')
        order_obj = sell_handler.get_order_by_token(token)
        order_obj.delete()
        return {"Result": "Order canceled"}
