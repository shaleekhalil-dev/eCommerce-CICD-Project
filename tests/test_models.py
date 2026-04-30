import unittest
from service.models import Product, Category, db
from tests.factories import ProductFactory
from . import app

class TestProductModel(unittest.TestCase):
    def test_read_a_product(self):
        product = ProductFactory()
        product.create()
        self.assertIsNotNone(product.id)
        found = Product.find(product.id)
        self.assertEqual(found.id, product.id)
        self.assertEqual(found.name, product.name)
        self.assertEqual(found.description, product.description)

    def test_update_a_product(self):
        product = ProductFactory()
        product.create()
        original_id = product.id
        product.description = "updated description"
        product.update()
        self.assertEqual(product.id, original_id)
        self.assertEqual(product.description, "updated description")
        self.assertEqual(len(Product.all()), 1)

    def test_delete_a_product(self):
        product = ProductFactory()
        product.create()
        self.assertEqual(len(Product.all()), 1)
        product.delete()
        self.assertEqual(len(Product.all()), 0)
