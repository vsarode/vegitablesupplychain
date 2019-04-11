from flask import request

from vegitablesupplychain.service_apis_handler import user_handler
from vegitablesupplychain.utils.resource import BaseResource
from vegitablesupplychain.view.user_view import UserView, HotelUserView


class User(BaseResource):
    def post(self):
        request_data = request.get_json(force=True)
        user_object = user_handler.create_user_object(request_data)
        if user_object.usertype == "FARMER":
            view = UserView()
            return view.render(user_object)
        else:
            view = HotelUserView()
            return view.render(user_object)


    def get(self, username=None):
        if username:
            user_object = user_handler.get_user_profile(username)
            if user_object.usertype == "FARMER":
                view = UserView()
                return view.render(user_object)
            else:
                view = HotelUserView()
                return view.render(user_object)
        criteria = request.args
        req_filter = {}
        if 'gstnNumber' in criteria:
            req_filter['gstn_no'] = criteria['gstnNumber']
            return user_handler.get_hotel_user_json(user_handler.get_hotel_user_by_filter(req_filter))
        if 'hotelName' in criteria:
            req_filter['hotel_name'] = criteria['hotelName']
            return {"hotels": [user_handler.get_hotel_user_json(hotel_obj) for hotel_obj in
                               user_handler.get_hotel_user_by_filter(req_filter)]}
        if ('userType', 'pincode') in criteria:
            req_filter['usertype'] = criteria['userType']
            req_filter['address__pincode'] = criteria['pincode']
            return {"users": [user_handler.get_user_json(user_obj) for user_obj in
                              user_handler.get_user_by_filter(req_filter)]}
        if 'userType' in criteria:
            req_filter['usertype'] = criteria['userType']
            return {"users": [user_handler.get_user_json(user_obj) for user_obj in
                              user_handler.get_user_by_filter(req_filter)]}
