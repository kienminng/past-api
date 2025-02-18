from custormer.entities.BaseEntities import BaseEntity
from custormer.entities.Product import Product


class Order(BaseEntity):
    product : Product
    product_id : int
    quantity : int

    def __init__(self, product , product_id, quantity):
        super().__init__()
        self.product = product
        self.product_id = product_id
        self.quantity = quantity

