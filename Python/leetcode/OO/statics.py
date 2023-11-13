class MyClass:
    static_variable = "I'm a static variable"

    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method():
        print("This is a static method")
        print(MyClass.static_variable)
    
    @staticmethod
    def change_static(message):
        MyClass.static_variable = message

    def instance_method(self):
        print("This is an instance method")
        print(self.instance_variable)
        print(MyClass.static_method())

# Usage:
obj = MyClass(42)
obj2 = MyClass(43)

obj.static_method()     # Calling a static method
obj2.static_method()
obj.static_variable = "I changed it obj1 here"
obj.static_method()     # Calling a static method
obj2.static_method()

obj.change_static("I changed it obj1 here")
obj.static_method()     # Calling a static method
obj2.static_method()

# obj.instance_method()   # Calling an instance method
# print(obj.static_variable)  # Accessing a static variable from an instance
