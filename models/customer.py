class Customer:

    def __init__(self, customer_id: int, customer_name: str):
        self.customer_id = customer_id
        self.customer_name = customer_name

    def __str__(self):
        return f"Customer name: {self.customer_name}, customer id: {self.customer_id} "
