import os

from flask import request
from werkzeug.utils import secure_filename

from vegitablesupplychain.constants import file_path
from vegitablesupplychain.db.supplychainmodels.models import SellOrders, Farmer
from vegitablesupplychain.service_apis_handler import sell_handler, user_handler
from vegitablesupplychain.utils.exceptions import AlreadyExist, \
    GenericCustomException
from vegitablesupplychain.utils.resource import BaseResource
from vegitablesupplychain.view.sell_order_view import SellOrderView


class SellOrderApi(BaseResource):
    def post(self):
        request_data = request.form.to_dict()
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(file_path.FILE_PATH, filename))
        request_data['productPic'] = filename
        order = sell_handler.place_sell_order(request_data)
        view = SellOrderView()
        return view.render(order)


    def get(self):
        data = request.args
        username =data['userId']
        user_object = user_handler.get_user_profile(username)
        if isinstance(user_object, Farmer):
            orders = sell_handler.get_order_by_username(username)
            view = SellOrderView()
            return {
                 "SellOrders": [view.render(order) for order
                                in orders]}
        else:
            orders = sell_handler.get_in_stock_products(data)
            return {"Products":[sell_handler.get_order_response_for_hotel(order, user_object) for order
                                in orders]}

    # def put(self):
    #     request_data = request.get_json(force=True)
    #     token = request.headers.get('token')
    #     order_obj = sell_handler.get_order_by_token(token)
    #     order_obj.farmer = user_handler.get_user_profile(request_data['userId'])
    #     order_obj.total_price = request_data['totalPrice']
    #     order_obj.shipping_address = sell_handler.update_shipping_address(
    #         order_obj, request_data)
    #     sell_handler.update_cart_items(order_obj, request_data)
    #     return sell_handler.get_order_json(order_obj)

    def delete(self, sale_order_id):
        order_obj = sell_handler.get_order_by_token(sale_order_id)
        if order_obj.is_shipped:
            raise GenericCustomException(message="Can't delete Already purchase by customer !!")
        order_obj.delete()
        return {"Result": "Order canceled"}
