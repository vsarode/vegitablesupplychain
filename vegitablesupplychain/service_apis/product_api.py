from flask import request

from vegitablesupplychain.service_apis_handler import product_handler
from vegitablesupplychain.utils.resource import BaseResource


class ProductApi(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        product_obj= product_handler.create_product(request_data)
        return product_handler.get_product_json(product_obj)


    def get(self):
        criteria = request.args
        req_filter={}
        if 'productName' in criteria:
            req_filter['product_name'] = criteria['productName']
        products = product_handler.get_product_by_filter(req_filter)
        return {'Products':[product_handler.get_product_json(product_obj) for product_obj in products]}


    def put(self,product_name):
        request_data = request.get_json(force=True)
        product_object = product_handler.update_product_data(product_name, request_data)
        return product_handler.get_product_json(product_object)