from models.order_in_mall import Order, Status


class Customer(Order):

    def __init__(self, customer_id: int, product_id: int, order_id: int, order_status: Status, customer_name: str):
        super().__init__(customer_id, product_id, order_id, order_status)
        self.customer_name = customer_name

    def __str__(self):
        return super().__str__() + f", customer name: {self.customer_name}"
