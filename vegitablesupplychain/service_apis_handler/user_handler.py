from vegitablesupplychain.db.supplychainmodels.models import User, \
    Farmer, Hotel, Address
from vegitablesupplychain.utils.exceptions import AlreadyExist, \
    NotFoundException
from vegitablesupplychain.view.user_view import HotelUserView, FarmerView, \
    UserView, AddressView


def create_user_profile(request_data):
    try:
        user = User.objects.get(username=request_data['userId'])
        raise AlreadyExist(user)
    except:
        user_type = request_data['userType']
        if user_type == 'Farmer':
            return Farmer.objects.create(
                user=create_user_object(request_data))
        else:
            return Hotel.objects.create(user=create_user_object(request_data),
                                        hotel_name=request_data['hotelName'],
                                        gstn_no=request_data['gstnNumber'],
                                        )


def create_user_object(request_data):
    user_obj = User.objects.create(username=request_data['userId'],
                               password=request_data['password'],
                               pan_no=request_data['panNumber'],
                               account_no=request_data['accountNumber'],
                               fullname=request_data['fullName'],
                               user_type=request_data['userType'],
                               mobile=request_data['mobile'],
                               photo=request_data['photo'],
                               )
    return user_obj


def get_user_profile(user_id):
    try:
        user_obj = User.objects.get(username=user_id)
        view = UserView()
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
    object.user.password = request_data["password"]
    object.user.mobile = request_data["mobile"]
    object.user.account_no = request_data["accountNumber"]
    object.user.pan_no = request_data["panNumber"]
    object.user.photo = request_data["photo"]
    update_addresses_of_user(username,request_data)
    object.save()
    return object


def update_hotel_data(username, request_data):
    object = get_user_profile(username)
    object.user.password = request_data["password"]
    object.user.mobile = request_data["mobile"]
    object.user.account_no = request_data["accountNumber"]
    object.user.pan_no = request_data["panNumber"]
    object.user.photo = request_data["photo"]
    object.hotel_name = request_data["hotelName"]
    update_addresses_of_user(username, request_data)
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


def update_addresses_of_user(username,request_data):
    print request_data
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


def update_address(obj,request_data):
    obj.address_line1 = request_data['addressLine1'],
    obj.address_line2 = request_data['addressLine2'],
    obj.state = request_data['state'],
    obj.district = request_data['district'],
    obj.taluka = request_data['taluka'],
    obj.village = request_data['village'],
    obj.pincode = request_data['pincode']
    obj.save()

