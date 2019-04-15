from flask import request

from vegitablesupplychain.service_apis_handler import user_handler
from vegitablesupplychain.utils.resource import BaseResource


class UserApi(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        user_object = user_handler.create_user_profile(request_data)
        if user_object.user.user_type == "Farmer":
            print user_object
            return user_handler.get_user_json(user_object)
        else:
            return user_handler.get_hotel_user_json(user_object)

    def get(self, username=None):
        if username:
            user_object = user_handler.get_user_profile(username)
            if user_object.user.user_type == "Farmer":
                return user_handler.get_user_json(user_object)
            else:
                return user_handler.get_hotel_user_json(user_object)
        criteria = request.args
        req_filter = {}
        if 'gstnNumber' in criteria:
            req_filter['gstn_no'] = criteria['gstnNumber']
            return user_handler.get_hotel_user_json(
                user_handler.get_hotel_user_by_filter(req_filter))
        if 'hotelName' in criteria:
            req_filter['hotel_name'] = criteria['hotelName']
            return {"Users": [user_handler.get_hotel_user_json(hotel_obj) for
                              hotel_obj in
                              user_handler.get_hotel_user_by_filter(
                                  req_filter)]}
        if ('userType', 'pincode') in criteria:
            req_filter['user_type'] = criteria['userType']
            req_filter['address__pincode'] = criteria['pincode']
            if criteria['userType'] == "Farmer":
                return {
                    "Users": [user_handler.get_user_json(user_obj) for user_obj
                              in
                              user_handler.get_user_by_filter(req_filter)]}
            else:
                return {
                    "Users": [user_handler.get_hotel_user_json(user_obj) for
                              user_obj
                              in
                              user_handler.get_user_by_filter(req_filter)]}
        if 'userType' in criteria:
            req_filter['user_type'] = criteria['userType']
            if criteria['userType'] == "Farmer":
                return {
                    "Users": [user_handler.get_user_json(user_obj) for user_obj
                              in
                              user_handler.get_user_by_filter(req_filter)]}
            else:
                return {
                    "Users": [user_handler.get_hotel_user_json(user_obj) for
                              user_obj
                              in
                              user_handler.get_user_by_filter(req_filter)]}

    def put(self, username):
        request_data = request.get_json(force=True)
        if request_data['userType'] == "Farmer":
            user_object = user_handler.update_farer_data(username, request_data)
            return user_handler.get_user_json(user_object)
        else:
            user_object = user_handler.update_hotel_data(username, request_data)
            return user_handler.get_hotel_user_json(user_object)
