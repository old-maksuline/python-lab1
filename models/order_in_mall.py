from models.order_status import Status


class Order:

    def __init__(self, order_id: int, customer_id: int, product_id: int, order_status: Status):
        self.order_id = order_id
        self.status = order_status
        self.product_id = product_id
        self.customer_id = customer_id

    def __str__(self):
        return f"Order id: {self.order_id}, status: {self.status}, product id: {self.product_id}," \
               f" customer id: {self.customer_id}"
