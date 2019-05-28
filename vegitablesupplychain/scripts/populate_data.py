import django;

django.setup()
from vegitablesupplychain.db.supplychainmodels.models import Product


def populate_products():

    _, _ = Product.objects.get_or_create(product_name='Potato',
                                         default_image='potato.jpg',
                                         # default_image='https://en.wikipedia.org/wiki/Potato#/media/File:Bamberger_Hoernle.jpg',
                                         features="1. Good \n 2. Best \n3.Better",
                                         price=102)
    _, _ = Product.objects.get_or_create(product_name='Tomato',
                                         default_image = 'tomato.jpg',
                                         # default_image='https://en.wikipedia.org/wiki/Tomato#/media/File:%E0%B0%9F%E0%B0%AE%E0%B0%BE%E0%B0%9F%E0%B0%BE%E0%B0%B2%E0%B1%81_(2).jpg',
                                         features="1. Good \n 2. Best \n3.Better",
                                         price=102)
    _, _ = Product.objects.get_or_create(product_name='Bringle',
                                         default_image='bringle.jpg',
                                         # default_image='https://en.wikipedia.org/wiki/Eggplant#/media/File:Solanum_melongena_24_08_2012_(1).JPG',
                                         features="1. Good \n 2. Best \n3.Better",
                                         price=102)
    print "Product populated successfully!!"


if __name__ == '__main__':
    populate_products()
