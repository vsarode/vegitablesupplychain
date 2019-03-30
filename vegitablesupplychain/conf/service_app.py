from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app, prefix='/supplychain/')
api.add_resource(User, 'user')
if __name__ == '__main__':
    app.run(host="localhost", port=2009, debug=True)
