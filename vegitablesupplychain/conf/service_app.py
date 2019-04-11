import django
django.setup()
from flask import Flask
from flask_restful import Api

from vegitablesupplychain.service_apis.user import UserApi

app = Flask(__name__)
api = Api(app, prefix='/supplychain/')
api.add_resource(UserApi, 'user','user/<username>')

if __name__ == '__main__':
    app.run(host="localhost", port=2009, debug=True)
