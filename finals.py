class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder(self, item)
    
class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")
        order.status = "delivered"

class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status

    def assign_driver(self, driver):
        self.driver = driver

    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer.name}\nStatus: {self.status}\nDriver: {self.driver.name}"

first_customer = Customer("Alice", "123")
second_customer = Customer("Bob", "456")
driver = Driver("David", "motorcycle")

first_customer.introduce()
second_customer.introduce()
driver.introduce()
print()
alice_order = DeliveryOrder(first_customer, "Laptop")
alice_order.assign_driver(driver)
bob_order = DeliveryOrder(second_customer, "Headphones")
bob_order.assign_driver(driver)
print(alice_order.summary())
print()
print(bob_order.summary())
print()
driver.deliver(alice_order)
driver.deliver(bob_order)
print()
print("Final Status:")
print(f"Order for {alice_order.item} → {alice_order.status}")
print(f"Order for {bob_order.item} → {bob_order.status}")