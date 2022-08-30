from models.product import Product


class Bread(Product):
    def __init__(self, product_id: int, product_type="baking"):
        super().__init__(product_id)
        self.product_type = product_type

    def __str__(self):
        return super().__str__() + f"product type: {self.product_type}, product: bread "
