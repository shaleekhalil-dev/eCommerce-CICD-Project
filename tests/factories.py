import factory
from service.models import Product, Category

class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    description = factory.Faker("text")
    # استخدام Faker لتوليد أسعار عشوائية لضمان التوافق
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    available = factory.Faker("boolean")
    category = factory.Iterator([
        Category.CLOTHS, Category.FOOD, Category.HOUSEWARES, 
        Category.AUTOMOTIVE, Category.TOOLS
    ])
