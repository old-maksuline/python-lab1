from models.bread import Bread
from models.milk import Milk
from models.accounting import Accounting
from models.customer import Customer
from models.order_in_mall import Order
from models.day import Day


def main():
    print("================================")

    customer1 = Customer(5, "Jack")
    customer2 = Customer(6, "James")

    print(customer1)
    print(customer2)

    product1 = Milk(25)
    product2 = Bread(26)
    product3 = Milk(28)

    print(product1)
    print(product2)
    print(product3)

    order1 = Order(1, customer1, product1)
    order2 = Order(2, customer2, product2, product3)

    accounting = Accounting()

    accounting.add_to_orders(order1, Day.MONDAY)
    accounting.add_to_orders(order2, Day.TUESDAY)
    accounting.print_orders()
    print("================================")


if __name__ == '__main__':
    main()
