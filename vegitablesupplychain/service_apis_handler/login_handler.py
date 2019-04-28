from vegitablesupplychain.db.supplychainmodels.models import Login, User
from vegitablesupplychain.utils.exceptions import NotFoundException
from vegitablesupplychain.view.login_view import LoginView


def get_login_json(login_obj):
    view = LoginView()
    return view.render(login_obj)


def get_login_objects_by_filter(criteria={}):
    return Login.object.filter(**criteria)


def get_login_object_by_token(token):
    try:
        return Login.objects.get(login_token=token)

    except:
        raise NotFoundException(token)



def get_user_object_by_token(token):
    try:
        login_obj = Login.objects.get(login_token=token)
        return User.objects.get(username=login_obj.user_username)
    except:
        raise NotFoundException(token)


def create_login(user_obj):
    login_obj = Login.objects.get_or_create(user=user_obj.user,is_logged_in=True)
    return login_obj
