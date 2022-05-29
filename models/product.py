from models.order_in_mall import Order, Status


class Product(Order):
    def __init__(self, customer_id: int, product_id: int, order_id: int, order_status: Status, product: str):
        super().__init__(customer_id, product_id, order_id, order_status)
        self.product = product

    def __str__(self):
        return super().__str__() + f", product: {self.product}"
