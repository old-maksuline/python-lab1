from models.product import Product
from models.accounting import Accounting
from models.customer import Customer
from models.order_in_mall import Order
from models.order_status import Status
from models.day import Day


def main():
    print("================================")
    order1 = Order(1, 225, 35, Status.ISSUED)
    order2 = Order(2, 226, 36, Status.ACCEPTED)
    customer1 = Customer(225, 35, 1, Status.ISSUED, "Jack")
    customer2 = Customer(226, 36, 2, Status.ACCEPTED, "James")
    print(customer1)
    print(customer2)
    product1 = Product(225, 35, 1, Status.ISSUED, "bread")
    product2 = Product(226, 36, 2, Status.ACCEPTED, "milk")
    print(product1)
    print(product2)
    accounting = Accounting()
    accounting.add_to_orders(order1, Day.MONDAY)
    accounting.add_to_orders(order2, Day.MONDAY)
    accounting.print_orders()
    print("================================")


if __name__ == '__main__':
    main()
