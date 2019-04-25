from vegitablesupplychain.db.supplychainmodels.models import User, \
    Farmer, Hotel, Address
from vegitablesupplychain.utils.exceptions import AlreadyExist, \
    NotFoundException, UnauthorisedException
from vegitablesupplychain.view.user_view import HotelUserView, FarmerView, \
    UserView, AddressView


def check_user_exist(request_data):
    if request_data['userType'] == 'Farmer':
        try:
            user = User.objects.get(username=request_data['userId'])
        except:
            return False
    elif request_data['userType'] == 'Hotel':
        try:
            hotel_obj = Hotel.objects.get(gstn_no=request_data['gstnNumber'])
        except:
            return False
    return True


def create_user_profile(request_data):
    user_type = request_data['userType']
    if user_type == 'Farmer':
        return Farmer.objects.create(
            user=create_user_object(request_data))
    else:
        return Hotel.objects.create(user=create_user_object(request_data),
                                    hotel_name=request_data['hotelName'],
                                    gstn_no=request_data['gstnNumber'])


def create_user_object(request_data):
    user_obj, created = User.objects.get_or_create(
        username=request_data['userId'])
    if created:
        user_obj.password = request_data['password']
        user_obj.pan_no = request_data['panNumber']
        user_obj.account_no = request_data['accountNumber']
        user_obj.fullname = request_data['fullName']
        user_obj.mobile = request_data['mobile']
        user_obj.photo = request_data['profilePic']
        user_obj.save()
    return user_obj


def get_farmer_by_user_id(user_id):
    try:
        farmer = Farmer.objects.get(user_username=user_id)
        return farmer
    except:
        raise NotFoundException(entity='Farmer')


def get_hotel_by_user_id(user_id):
    try:
        hotel = Hotel.objects.get(user_username=user_id)
        return hotel
    except:
        raise NotFoundException(entity='Hotel')


def get_user_profile(user_id):
    try:
        user_obj = User.objects.get(username=user_id)
        try:
           farmer_obj = Farmer.objects.get(user=user_obj)
           return farmer_obj
        except:
            try:
                hotel_obj = Hotel.objects.get(user=user_obj)
                return hotel_obj
            except:
                return {}
    except:
        raise NotFoundException(entity='User')


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


def update_farmer_data(object, request_data):
    object.user.password = request_data["password"]
    object.user.mobile = request_data["mobile"]
    object.user.account_no = request_data["accountNumber"]
    object.user.pan_no = request_data["panNumber"]
    object.user.photo = request_data["profilePic"]
    # update_addresses_of_user(username, request_data)
    object.user.save()
    return object


def update_hotel_data(object, request_data):
    object.user.password = request_data["password"]
    object.user.mobile = request_data["mobile"]
    object.user.account_no = request_data["accountNumber"]
    object.user.pan_no = request_data["panNumber"]
    object.user.photo = request_data["profilePic"]
    object.hotel_name = request_data["hotelName"]
    # update_addresses_of_user(username, request_data)
    object.user.save()
    object.save()
    return object


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


def get_address_json(obj):
    view = AddressView()
    return view.render(obj)


def get_address_object_by_id(id):
    try:
        return Address.objects.get(id=id)
    except:
        raise NotFoundException(id)


def get_shipping_addresses(addresses):
    address_list = [get_address_object_by_id(adr.id) for adr in addresses]
    return address_list


def get_addresses_by_username(username):
    user_obj = get_user_profile(username)
    return user_obj.user.shipping_addresses.all()


def update_addresses_of_user(username, request_data):
    obj = get_address_object_by_id(request_data['addressId'])
    obj.address_line1 = request_data['addressLine1']
    obj.address_line2 = request_data['addressLine2']
    obj.state = request_data['state']
    obj.district = request_data['district']
    obj.taluka = request_data['taluka']
    obj.village = request_data['village']
    obj.pincode = request_data['pincode']
    obj.save()
    return get_addresses_by_username(username)
