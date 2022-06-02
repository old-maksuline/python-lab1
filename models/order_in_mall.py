from models.customer import Customer
from models.product import Product


class Order:

    def __init__(self, order_id: int, customer: Customer, *product: Product):
        self.products = [*product]
        self.order_id = order_id
        self.customer = customer

    def __str__(self):
        return f"Order id: {self.order_id}, {self.customer.__str__()}, {''.join(map(str, self.get_products()))} "

    def get_customer(self):
        return self.customer

    def get_products(self):
        return self.products
