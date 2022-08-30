from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id: int):
        self.product_id = product_id

    @abstractmethod
    def __str__(self):
        return f"Prod id: {self.product_id}, "
