from vegitablesupplychain.db.supplychainmodels.models import User, Address, Farmer, Hotel
from vegitablesupplychain.utils.exceptions import AlreadyExist, NotFoundException
from vegitablesupplychain.view.user_view import HotelUserView, UserView


def create_user_profile(request_params):
    try:
        user = User.objects.get(username=request_params['userId'])
        raise AlreadyExist(user)
    except:
        user_type = request_params['userType']
        if user_type == 'FARMER':
            return Farmer.objects.create(user=create_user_object(request_params))
        else:
            return Hotel.objects.create(user=create_user_object(request_params),
                                        hotel_name=request_params['hotelName'],
                                        gstn_no=request_params['gstnNumber'],
                                        )


def create_user_object(request_params):
    return User.objects.create(username=request_params['userId'],
                               fname=request_params['firstName'],
                               mname=request_params['middleName'],
                               lname=request_params['lastName'],
                               gender=request_params['gender'],
                               usertype=request_params['userType'],
                               mobile=request_params['mobile'],
                               address=create_address_object(request_params)
                               )


def create_address_object(request_params):
    return Address.objects.create(
        address_line1=request_params['addressLine1'],
        address_line2=request_params['addressLine2'],
        state=request_params['state'],
        district=request_params['district'],
        taluka=request_params['taluka'],
        village=request_params['village'],
        pincode=request_params['pincode'],
    )


def get_user_profile(user_id):
    try:
        user = User.objects.get(username=user_id)
        if user.usertype == "FARMER":
            return Farmer.objects.get(user=user_id)
        else:
            return Hotel.objects.get(user=user_id)
    except:
        raise NotFoundException(user_id)


def get_hotel_user_by_filter(criteria={}):
    return Hotel.objects.filter(**criteria)


def get_user_by_filter(criteria={}):
    return User.objects.filter(**criteria)


def get_hotel_user_json(hotel_obj):
    view = HotelUserView()
    return view.render(hotel_obj)


def get_user_json(user_obj):
    view = UserView()
    return view.render(user_obj)
