'''
User

'''

from enum import Enum
from abc import ABC, abstractmethod

class Category(Enum):
    FURNITURE = 1
    ELECTRONICS = 2
    SPORTS = 3
    ACCESSORIES = 4

class OrderStatus(Enum):
    READY = 1
    PLACED = 2

class Product:

    def __init__(self, name, category):
        self.name = name
        self.category = category

class ProductFactory(ABC):
    @abstractmethod
    def createProduct(self, name):
        pass

class FurnitureProductFactory(ProductFactory):
    def createProduct(self, name):
        return Product(name, Category.FURNITURE)
    
class ElectronicsProductFactory(ProductFactory):
    def createProduct(self, name):
        return Product(name, Category.ELECTRONICS)
    
class AccessoriesProductFactory(ProductFactory):
    def createProduct(self, name):
        return Product(name, Category.ACCESSORIES)

class SportsProductFactory(ProductFactory):
    def createProduct(self, name):
        return Product(name, Category.SPORTS)

class ProductCatalog:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ProductCatalog, cls).__new__(cls)
            cls._instance.init_product_catalog()
        return cls._instance

    def init_product_catalog(self):
        self.product_catalog = {}
        categories = Category
        for category in categories:
            self.product_catalog[category.name] = {}

    def add_products_to_catalog(self, product, quantity):
        if product.category in self.product_catalog.keys():
            if product.name in self.product_catalog[product.category].keys():
                self.product_catalog[product.category][product.name] += quantity
            else:
                self.product_catalog[product.category][product.name] = quantity
    
    def is_product_available(self, product, quantity):
        if product.category in self.product_catalog.keys():
            if product.name in self.product_catalog[product.category].keys():
                if self.product_catalog[product.category][product.name] >= quantity:
                    return True
        return False
    
    def print_catalog(self):
        categories = Category
        for category in categories:
            print(f"{category.name} and {self.product_catalog[category.name]}")
            

class User:

    def __init__(self, name):
        self.name = name
        self.active_orders = {}
        self.placed_orders = {}
    
    def start_order(self):
        order = Order()
        self.active_orders[order.id] = order
        return order.id

    def add_product_to_order(self, id, product, quantity):
        if CATALOG.is_product_available(product, quantity):
            order = self.active_orders[id]
            order.add_product(product, quantity)

    def remove_product_from_order(self, id, product, quantity):
        order = self.active_orders[id]
        order.remove_product(product, quantity)

    def place_order(self, id):
        order = self.active_orders[id]
        order.place_order()
        del self.active_orders[id]
        self.placed_orders[id] = order

    def get_placed_order_details(self, id):
        if id in self.placed_orders:
            print(self.placed_orders[id])
        else:
            print(f"{id} order not found in placed orders")

    def get_active_order_details(self, id):
        if id in self.active_orders:
            print(self.active_orders[id])
        else:
            print(f"{id} order not found in active orders")

class Order:
    order_id = 1

    def __init__(self):
        self.id = Order.order_id
        Order.inc_order_id()
        self.product_quantity_mapping = {}

    def __str__(self):
        str = ""
        for key in self.product_quantity_mapping.keys():
            str += (f"{key} and quantity {self.product_quantity_mapping[key]}\n")
        return str

    @staticmethod
    def inc_order_id():
        Order.order_id += 1

    def add_product(self, product, quantity):
        if product in self.product_quantity_mapping:
            self.product_quantity_mapping[product] += quantity
        else:
            self.product_quantity_mapping[product] = quantity
        
    def remove_product(self, product, quantity):
        if product in self.product_quantity_mapping and self.product_quantity_mapping[product] >= quantity:
            self.product_quantity_mapping[product] -= quantity
            return True
        else:
            return False
    
    def place_order(self):
        self.order_status = OrderStatus.PLACED

CATALOG = ProductCatalog()
def create_product_catalog():
    for product_name in ["pr1", "pr2"]:
        CATALOG.add_products_to_catalog(FurnitureProductFactory().createProduct(product_name), 10)
        CATALOG.add_products_to_catalog(ElectronicsProductFactory().createProduct(product_name), 10)
        CATALOG.add_products_to_catalog(SportsProductFactory().createProduct(product_name), 10)
        CATALOG.add_products_to_catalog(AccessoriesProductFactory().createProduct(product_name), 10)

create_product_catalog()
CATALOG.print_catalog()
user = User("ninad")
order_1_id = user.start_order()
print(order_1_id)
user.add_product_to_order(order_1_id, Product("pr1", Category.FURNITURE), 10)
user.get_active_order_details(order_1_id)


class Singleton:
    _instance = None

    def __new__(cls, param1, param2):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton(param1, param2)
        return cls._instance
    
    def init_singleton(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    



    

