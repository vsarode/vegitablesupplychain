import django;


django.setup()

from flask import Flask
from flask_restful import Api

from vegitablesupplychain.service_apis.user import UserApi
from vegitablesupplychain.service_apis.loginapi import LoginApi
from vegitablesupplychain.service_apis.product_api import ProductApi
from vegitablesupplychain.service_apis.order_api import PurchaseOrderApi
from vegitablesupplychain.service_apis.address_api import AddressApi
from vegitablesupplychain.service_apis.sell_api import SellOrderApi
from vegitablesupplychain.service_apis.cart import Cart


app = Flask(__name__)
api = Api(app, prefix='/supplychain/')
api.add_resource(UserApi, 'user','user/<username>')
api.add_resource(LoginApi, 'login','login/<token>')
api.add_resource(ProductApi, 'product','product/<product_name>')
api.add_resource(PurchaseOrderApi, 'order','order/<order_token>')
api.add_resource(SellOrderApi, 'sell','sell/<sale_order_id>')
api.add_resource(Cart, 'cart','cart/<username>')
api.add_resource(AddressApi, 'address','address/<id>')


if __name__ == '__main__':
    app.run(host="localhost", port=2009, debug=True)
