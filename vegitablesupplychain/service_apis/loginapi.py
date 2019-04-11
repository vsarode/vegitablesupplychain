from flask import request, current_app, jsonify

from flask_restful import Resource

from MyProject.db.user_models.models import User, Login
from MyProject.service_apis_handler import login_handler, user_handler


class LoginApi(Resource):
    def post(self):
        bodyprams = request.get_json()
        user_object = user_handler.get_user_by_username(bodyprams['username'])
        if user_object.password == bodyprams['password']:
            loggin_obj, _ = login_handler.create_login(user_object)
            print loggin_obj
            return jsonify({"login":login_handler.get_login_json(loggin_obj)})

    def get(self, token):
        if token:
            loggin_object = Login.objects.filter(token=token)
            return jsonify({"login":login_handler.get_login_json(loggin_object)})
        criteria=request.args
        req_filter={}
        if 'username' in criteria:
            req_filter['user_id'] = criteria['username']
        if 'firstName' in criteria:
            req_filter['user__fname'] = criteria['firstName']
        return jsonify({"login":[login_handler.get_login_json(login_obj) for login_obj in login_handler.get_login_objects_by_filter(req_filter)]})