from datetime import datetime
from flask import request
from flask_restful import Resource

from vegitablesupplychain.service_apis_handler import user_handler, \
    login_handler
from vegitablesupplychain.utils.exceptions import UnauthorisedException, \
    BadRequest


class LoginApi(Resource):
    def post(self):
        bodyprams = request.get_json()
        user_object = user_handler.get_user_profile(bodyprams['username'])
        if user_object.user.password == bodyprams['password']:
            loggin_obj, _ = login_handler.create_login(user_object)
            return login_handler.get_login_json(loggin_obj)
        else:
            raise UnauthorisedException()

    def get(self, token):
        if token:
            user_object = login_handler.get_user_object_by_token(token)
            if user_object.user.user_type == 'Farmer':
                return user_handler.get_user_json(user_object)
            else:
                return user_handler.get_hotel_user_json(user_object)
        else:
            raise BadRequest()

    def put(self, token):
        if token:
            login_object = login_handler.get_login_object_by_token(token)
            login_object.is_logged_in = False
            login_object.loggedout_time = datetime.now()
            print datetime.now()
            login_object.save()
            # print login_object.logged_out_time
            return login_handler.get_login_json(login_object)
        else:
            raise BadRequest()
