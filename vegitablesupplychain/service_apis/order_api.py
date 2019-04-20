from flask import request

from vegitablesupplychain.service_apis_handler import order_handler
from vegitablesupplychain.utils.resource import BaseResource


class PurchaseOrderApi(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        order = order_handler.place_purchase_order(request_data)
        return order_handler.get_order_json(order)

    def get(self, username=None):
        if username:
            orders = order_handler.get_order_by_username(username)
            return {
                "PurchaseOrders": [order_handler.get_order_json(order) for order
                                   in orders]}
        token = request.headers.get('token')
        if token:
            order_obj = order_handler.get_order_by_token(token)
            return order_handler.get_order_json(order_obj)

    def put(self):
        request_data = request.get_json(force=True)
        token = request.headers.get('token')
        order_obj = order_handler.get_order_by_token(token)
        order_obj.total_price = request_data['totalPrice']
        order_obj.shipping_address = order_handler.update_shipping_address(
            order_obj, request_data)
        order_handler.update_cart_items(order_obj, request_data)
        return order_handler.get_order_json(order_obj)

    def delete(self):
        token = request.headers.get('token')
        order_obj = order_handler.get_order_by_token(token)
        order_obj.delete()
        return {"Result": "Order canceled"}
