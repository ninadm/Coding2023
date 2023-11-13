'''
Restaurant Management:

Restaurants can register and log in to the system.
Each restaurant should be able to manage its menu, including adding, updating, and removing items.
Order Placement and Fulfillment:

Customers can browse menus, add items to their cart, and place orders.
Once an order is placed, the restaurant receives the order details and starts preparing the food.
The system should keep track of the order status (received, preparing, ready, delivered).


Users
Food items
Order
    user
    food items

Menus
    food items
Restaraunt
    name, 
    food items

'''

from enum import Enum

class OrderStatus(Enum):
    PREPARING = 2
    RECEIVED = 1
    READY = 3
    DELIVERED = 4


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    

class FoodItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Menu:

    def __init__(self, foods=[]):
        self.items = foods
    
    def addItem(self, foodItem):
        self.items.append(foodItem)
    
    def updateItem(self, foodItem):
        for item in self.items:
            if item.name == foodItem.name:
                item.price = foodItem.price
                item.category = foodItem.category
                if foodItem.newName:
                    item.name = foodItem.newName
    
    def deleteItem(self, foodItem):
        print(f'Currently {len(self.items)} elements present')
        for i in range(len(self.items)):
            if self.items[i].name == foodItem.name:
                self.items[i], self.items[-1] = self.items[-1], self.items[i]
                del self.items[-1]
        print(f'After deletion {len(self.items)} elements present')

class Restaraunt:
    def __init__(self, name, address, menu):
        self.name = name
        self.address = address
        self.menu = menu

class Order:

    def __init__(self, user, items, status = OrderStatus.RECEIVED):
        self.user = user
        self.items = items
        self.status = status

    def updateStatus(self, status):
        self.status = status

class Cart:

    def __init__(self, user):
        self.user = user
    
    def addItem(self, item, quantity):
        pass

    def removeItem(self, item, quantity):
        pass

    def deleteItem(self, item):
        pass