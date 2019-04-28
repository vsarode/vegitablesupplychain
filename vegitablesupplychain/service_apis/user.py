import os

from flask import request
from werkzeug.utils import secure_filename

from vegitablesupplychain.constants import file_path
from vegitablesupplychain.db.supplychainmodels.models import Farmer
from vegitablesupplychain.service_apis_handler import user_handler
from vegitablesupplychain.utils.exceptions import AlreadyExist
from vegitablesupplychain.utils.resource import BaseResource
from vegitablesupplychain.view.user_view import  HotelUserView, \
    FarmerFullView


class UserApi(BaseResource):
    def post(self):
        request_data = request.form.to_dict()
        if user_handler.check_user_exist(request_data):
            raise AlreadyExist(entity='User')
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(file_path.FILE_PATH, filename))
        request_data['profilePic'] = filename
        user_object = user_handler.create_user_profile(request_data)
        if isinstance(user_object, Farmer):
            view = FarmerFullView()
            return view.render(user_object)
        else:
            view = HotelUserView()
            return view.render(user_object)

    def get(self, username=None):
        if username:
            user_object = user_handler.get_user_profile(username)
            if isinstance(user_object, Farmer):
                view = FarmerFullView()
                return view.render(user_object)
            else:
                view = HotelUserView()
                return view.render(user_object)
        criteria = request.args
        req_filter = {}
        if 'gstnNumber' in criteria:
            req_filter['gstn_no'] = criteria['gstnNumber']
            view = HotelUserView()
            return user_handler.get_hotel_user_json(
                user_handler.get_hotel_user_by_filter(req_filter))
        if 'hotelName' in criteria:
            req_filter['hotel_name'] = criteria['hotelName']
            view = HotelUserView()
            return {"Users": [view.render(hotel_obj) for
                              hotel_obj in
                              user_handler.get_hotel_user_by_filter(
                                  req_filter)]}

    def put(self, username):
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(file_path.FILE_PATH, filename))
        request_data = request.form.to_dict()
        request_data['profilePic'] = filename
        user_object = user_handler.get_user_profile(username)
        if isinstance(user_object, Farmer):
            user_object = user_handler.update_farmer_data(user_object,
                                                          request_data)
            view = FarmerFullView()
            return view.render(user_object)
        else:
            user_object = user_handler.update_hotel_data(user_object,
                                                         request_data)
            view = HotelUserView()
            return view.render(user_object)
