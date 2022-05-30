from models.day import Day
from models.order_in_mall import Order


class Accounting:
    orders = {
        Day.MONDAY: [],
        Day.TUESDAY: [],
        Day.WEDNESDAY: [],
        Day.THURSDAY: [],
        Day.FRIDAY: [],
        Day.SATURDAY: [],
        Day.SUNDAY: [],
    }

    def add_to_orders(self, order: Order, day: Day):
        self.orders[day].append(order)

    def print_orders(self):
        for key, value in self.orders.items():
            if value:
                print("%s: {" % key)
                for val in value:
                    print(val)
                print('}')
