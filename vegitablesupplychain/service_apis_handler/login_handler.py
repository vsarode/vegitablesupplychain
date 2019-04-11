import uuid

from flask import current_app

from MyProject.db.user_models.models import Login
from MyProject.service_apis_handler import user_handler


def get_login_json(login_obj):
    return {
                "loginToken": login_obj.token,
                "isLoggedIn": login_obj.is_logged_in,
                "createdOnTime":login_obj.created_on.strftime("%d/%m/%Y"),
                "loggedOutTime":login_obj.loggedout_time.strftime("%d/%m/%Y") if login_obj.loggedout_time else "",
                "user": user_handler.get_user_json(login_obj.userid)
            }

def get_login_objects_by_filter(criteria={}):
    return Login.object.filter(**criteria)

def get_login_objects_by_token(token):
    try:
        login_obj = Login.objects.get(token=token)
        return login_obj
    except:
        raise Exception()


def create_login(user):
    login_obj = Login.objects.get_or_create(userid=user,is_logged_in=True)
    return login_obj
