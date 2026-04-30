import logging
from enum import Enum
from decimal import Decimal
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""

class Category(Enum):
    UNKNOWN = 0
    CLOTHS = 1
    FOOD = 2
    HOUSEWARES = 3
    AUTOMOTIVE = 4
    TOOLS = 5

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    available = db.Column(db.Boolean(), nullable=False, default=True)
    category = db.Column(db.Enum(Category), nullable=False, server_default=(Category.UNKNOWN.name))

    def create(self):
        self.id = None
        db.session.add(self)
        db.session.commit()

    def update(self):
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "available": self.available,
            "category": self.category.name
        }

    def deserialize(self, data: dict):
        try:
            self.name = data["name"]
            self.description = data["description"]
            self.price = Decimal(data["price"])
            self.available = data["available"]
            self.category = getattr(Category, data["category"])
        except Exception as error:
            raise DataValidationError("Invalid product data: " + str(error))
        return self

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, product_id):
        return cls.query.get(product_id)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(cls.name == name)

    @classmethod
    def find_by_category(cls, category):
        return cls.query.filter(cls.category == category)

    @classmethod
    def find_by_availability(cls, available):
        return cls.query.filter(cls.available == available)
