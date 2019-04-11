from vegitablesupplychain.db.supplychainmodels.models import User, Address, \
    Farmer, Hotel
from vegitablesupplychain.utils.exceptions import AlreadyExist, \
    NotFoundException
from vegitablesupplychain.view.user_view import HotelUserView, FarmerView, \
    UserView


def create_user_profile(request_data):
    try:
        user = User.objects.get(username=request_data['userId'])
        raise AlreadyExist(user)
    except:
        user_type = request_data['userType']
        print user_type
        if user_type == 'Farmer':
            return Farmer.objects.create(
                user=create_user_object(request_data))
        else:
            return Hotel.objects.create(user=create_user_object(request_data),
                                        hotel_name=request_data['hotelName'],
                                        gstn_no=request_data['gstnNumber'],
                                        )


def create_user_object(request_data):
    return User.objects.create(username=request_data['userId'],
                               password=request_data['password'],
                               pan_no=request_data['panNumber'],
                               account_no=request_data['accountNumber'],
                               fullname=request_data['fullName'],
                               user_type=request_data['userType'],
                               mobile=request_data['mobile'],
                               photo=request_data['photo'],
                               address=create_address_object(request_data)
                               )


def create_address_object(request_data):
    return Address.objects.create(
        address_line1=request_data['addressLine1'],
        address_line2=request_data['addressLine2'],
        state=request_data['state'],
        district=request_data['district'],
        taluka=request_data['taluka'],
        village=request_data['village'],
        pincode=request_data['pincode'],
    )


def get_user_profile(user_id):
    try:
        user_obj = User.objects.get(username=user_id)
        view = UserView()
        print view.render(user_obj)
        if user_obj.user_type == "Farmer":
            return Farmer.objects.get(user=user_obj)
        else:
            return Hotel.objects.get(user=user_obj)
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
    view = FarmerView()
    return view.render(user_obj)


def update_farmer_data(username, request_data):
    object = get_user_profile(username)
    object.user.address.address_line1 = request_data['addressLine1']
    object.user.address.address_line2 = request_data['addressLine2']
    object.user.address.state = request_data['state']
    object.user.address.district = request_data['district']
    object.user.address.taluka = request_data['taluka']
    object.user.address.village = request_data['village']
    object.user.address.pincode = request_data['pincode']
    object.user.password = request_data["password"]
    object.user.mobile = request_data["mobile"]
    object.user.account_no = request_data["accountNumber"]
    object.user.pan_no = request_data["panNumber"]
    object.user.photo = request_data["photo"]
    object.save()
    return object

def update_hotel_data(username, request_data):
    object = get_user_profile(username)
    object.user.address.address_line1 = request_data['addressLine1']
    object.user.address.address_line2 = request_data['addressLine2']
    object.user.address.state = request_data['state']
    object.user.address.district = request_data['district']
    object.user.address.taluka = request_data['taluka']
    object.user.address.village = request_data['village']
    object.user.address.pincode = request_data['pincode']
    object.user.password = request_data["password"]
    object.user.mobile = request_data["mobile"]
    object.user.account_no = request_data["accountNumber"]
    object.user.pan_no = request_data["panNumber"]
    object.user.photo = request_data["photo"]
    object.hotel_name = request_data["hotelName"]
    object.save()
    return object