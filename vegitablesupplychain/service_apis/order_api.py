from flask import request

from vegitablesupplychain.service_apis_handler import order_handler
from vegitablesupplychain.utils.resource import BaseResource


class PurchaseOrderApi(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        order_obj = order_handler.place_purchase_order(request_data)
        return order_handler.get_order_json(order_obj)


    def get(self):
        data = request.args
        username = data['userId']
        orders = order_handler.get_order_by_username(username)
        return {
                "PurchaseOrders": [order_handler.get_order_json(order) for order
                                   in orders]}


    def delete(self,order_token):
        order_obj = order_handler.get_order_by_token(order_token)
        order_handler.delete_purchase_order_action(order_obj)
        order_obj.delete()
        return {"Result": "Order canceled"}
