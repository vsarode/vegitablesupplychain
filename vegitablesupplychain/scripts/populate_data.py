import django;

django.setup()
from vegitablesupplychain.db.supplychainmodels.models import Brand, Category, \
    Product


def populate_brands():
    _, _ = Brand.objects.get_or_create(brand_name='Brand1')
    _, _ = Brand.objects.get_or_create(brand_name='Brand2')
    _, _ = Brand.objects.get_or_create(brand_name='Brand3')
    _, _ = Brand.objects.get_or_create(brand_name='Brand4')
    print "Brand populated successfully!!"


def populate_category():
    _, _ = Category.objects.get_or_create(category_name="category1")
    _, _ = Category.objects.get_or_create(category_name="category2")
    _, _ = Category.objects.get_or_create(category_name="category3")
    _, _ = Category.objects.get_or_create(category_name="category4")

    print "Categor populated successfully!!"


def populate_products():
    brand1 = Brand.objects.first()
    brand2 = Brand.objects.last()

    category1 = Category.objects.first()
    category2 = Category.objects.last()

    _, _ = Product.objects.get_or_create(product_name='Potato',
                                         category=category1,
                                         brand=brand1,
                                         default_image='potato.jpg',
                                         # default_image='https://en.wikipedia.org/wiki/Potato#/media/File:Bamberger_Hoernle.jpg',
                                         features="1. Good \n 2. Best \n3.Better",
                                         price=102)
    _, _ = Product.objects.get_or_create(product_name='Tomato',
                                         category=category1,
                                         brand=brand1,
                                         default_image = 'tomato.jpg',
                                         # default_image='https://en.wikipedia.org/wiki/Tomato#/media/File:%E0%B0%9F%E0%B0%AE%E0%B0%BE%E0%B0%9F%E0%B0%BE%E0%B0%B2%E0%B1%81_(2).jpg',
                                         features="1. Good \n 2. Best \n3.Better",
                                         price=102)
    _, _ = Product.objects.get_or_create(product_name='Bringle',
                                         category=category2,
                                         brand=brand2,
                                         default_image='bringle.jpg',
                                         # default_image='https://en.wikipedia.org/wiki/Eggplant#/media/File:Solanum_melongena_24_08_2012_(1).JPG',
                                         features="1. Good \n 2. Best \n3.Better",
                                         price=102)
    print "Product populated successfully!!"


if __name__ == '__main__':
    populate_brands()
    populate_category()
    populate_products()
