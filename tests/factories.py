import factory
from factory import fuzz
from service.models import Product, Category

class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    description = factory.Faker("text")
    price = fuzz.FuzzyDecimal(0.5, 2000.0, 2)
    available = factory.Faker("boolean")
    category = factory.Iterator([
        Category.CLOTHS, Category.FOOD, Category.HOUSEWARES, 
        Category.AUTOMOTIVE, Category.TOOLS
    ])
