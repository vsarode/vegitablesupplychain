from vegitablesupplychain.db.supplychainmodels.models import Product
from vegitablesupplychain.utils.exceptions import AlreadyExist, \
    NotFoundException
from vegitablesupplychain.view.product_view import ProductView


def create_product(request_data):
    try:
        product_obj = Product.objects.get(
            product_name=request_data["productName"])
        raise AlreadyExist(product_obj)
    except:
        return Product.objects.create(product_name=request_data["productName"],
                                      default_image=request_data[
                                          "productImage"],
                                      features=request_data["features"],
                                      price=request_data["price"])



def get_product_json(product_obj):
    view = ProductView()
    return view.render(product_obj)


def get_product_by_name(product_name):
    try:
        return Product.objects.get(product_name=product_name)
    except:
        raise NotFoundException(entity='Product')


def get_product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except:
        raise NotFoundException(entity='Product')


def get_product_by_filter(criteria={}):
    return Product.objects.filter(**criteria)


def update_product_data(product_name, request_data):
    product_obj = get_product_by_name(product_name)
    product_obj.features = request_data['features']
    product_obj.price = request_data['price']
    product_obj.save()
    return product_obj
